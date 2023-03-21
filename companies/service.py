from django.contrib.auth.models import User

from .models import Company, Deal, Employee
from .serializers import CompanySerializer


class CompanyStatsService:
    @property
    def most_recently_founded_companies(self, limit=10, serialized=True):
        companies = Company.companies.most_recently_founded()
        
        if serialized:
            return CompanySerializer(companies, many=True).data

        return companies

    @property
    def companies_founded_per_quarter(self, serialized=True):
        companies = Company.companies.companies_founded_per_quarter()

        if serialized:
            return self._serialize_companies_per_quarter(companies)

        return companies

    @property
    def average_employee_count(self):
        return Company.companies.avg_employee_count()

    @property
    def user_with_most_companies(self):
        user_id = Company.companies.user_with_most_companies()
        return User.objects.get(id=user_id).username

    @property
    def user_with_most_employees(self):
        user_id = Employee.employees.user_with_most_employees()
        return User.objects.get(id=user_id).username

    @property
    def average_deal_amounts_by_country(self, serialized=True):
        deals = Deal.deals.avg_deals_amounts_by_country()

        if serialized:
            return self._serialize_deal_amounts_by_country(deals)

        return deals

    def get_company_stats(self):
        return {
            'most_recently_founded': self.most_recently_founded_companies,
            'average_employee_count': self.average_employee_count,
            'companies_founded_per_quarter': self.companies_founded_per_quarter,
            'user_created_most_companies': self.user_with_most_companies,
            'user_created_most_employees': self.user_with_most_employees,
            'average_deal_amount_raised_by_country': self.average_deal_amounts_by_country
        }

    def _serialize_companies_per_quarter(self, companies_per_quarter):
        serialized = []

        for data in companies_per_quarter:
            serialized.append({
                'quarter': ((data['quarter'].month-1) // 3) + 1,
                'count': data['count'],
                'year': data['year']
            })

        return serialized

    def _serialize_deal_amounts_by_country(self, deals):
        serialized = []

        for data in deals:
            serialized.append({
                'country': data['company__country__name'],
                'avg_amount_raised': data['avg_amount_raised']
            })

        return serialized
