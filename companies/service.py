import datetime

from django.db.models import Avg, Count, Sum
from django.db.models.functions import ExtractYear, TruncQuarter
from django.contrib.auth.models import User

from .models import Company, Employee, Deal
from .serializers import CompanySerializer


class CompanyStatsService:
    def __init__(self):
        self._all_companies = None

    @property
    def all_companies(self):
        if self._all_companies is None:
            self._all_companies = Company.objects.all()
        return self._all_companies
    
    @property
    def most_recently_founded_companies(self, limit=10):
        companies = self.all_companies[:limit]
        serializer = CompanySerializer(companies, many=True)
        return sorted(serializer.data, key=lambda comp: comp['date_founded'])

    @property
    def companies_founded_per_quarter(self):
        return self._get_companies_founded_per_quarter()

    @property
    def average_employee_count(self):
        return Company.objects.annotate(num_employees=Count('employee')).aggregate(Avg('num_employees'))['num_employees__avg']

    @property
    def user_with_most_companies(self):
        user_id = Company.objects.values('creator').annotate(num_companies=Count('id')).order_by('-num_companies').first()['creator']
        return User.objects.get(id=user_id).username

    @property
    def user_with_most_employees(self):
        user_id = Employee.objects.values('company__creator').annotate(total_employees=Sum('company__employee__id')).order_by('-total_employees').first()['company__creator']
        return User.objects.get(id=user_id).username

    @property
    def average_deal_amounts_by_country(self):
        return self._get_average_deal_amounts_by_country()

    def get_company_stats(self):
        return {
            'most_recently_founded': self.most_recently_founded_companies,
            'average_employee_count': self.average_employee_count,
            'companies_founded_per_quarter': self.companies_founded_per_quarter,
            'user_created_most_companies': self.user_with_most_companies,
            'user_created_most_employees': self.user_with_most_employees,
            'average_deal_amount_raised_by_country': self.average_deal_amounts_by_country
        }

    def _get_companies_founded_per_quarter(self):
        five_years_ago = datetime.date.today() - datetime.timedelta(days=5*365)

        companies_per_quarter = (
            Company.objects.annotate(
                quarter=TruncQuarter('date_founded'),
                year=ExtractYear('date_founded')
            )
            .filter(date_founded__gte=five_years_ago)
            .values('quarter', 'year')
            .annotate(count=Count('id'))
            .order_by('-year', '-quarter')
        )

        serialized = []
        for data in companies_per_quarter:
            serialized.append({
                'quarter': ((data['quarter'].month-1) // 3) + 1,
                'count': data['count'],
                'year': data['year']
            })

        return serialized

    def _get_average_deal_amounts_by_country(self):
        avg_deals_by_country = Deal.objects.values('company__country__name').annotate(avg_amount_raised=Avg('amount_raised')).order_by('-avg_amount_raised').values('company__country__name', 'avg_amount_raised')

        serialized = []
        for data in avg_deals_by_country:
            serialized.append({
                'country': data['company__country__name'],
                'avg_amount_raised': data['avg_amount_raised']
            })

        return serialized
