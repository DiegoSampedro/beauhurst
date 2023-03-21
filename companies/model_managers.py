import datetime

from django.db import models
from django.db.models import Avg, Count, Sum
from django.db.models.functions import ExtractYear, TruncQuarter


class CompanyQuerySet(models.QuerySet):
    def most_recently_founded(self, limit):
        return self.order_by('-date_founded')[:limit]

    def avg_employee_count(self):
        return self.annotate(num_employees=Count('employee')).aggregate(Avg('num_employees'))['num_employees__avg']

    def user_with_most_companies(self):
        return self.values('creator').annotate(num_companies=Count('id')).order_by('-num_companies').first()['creator']

    def companies_founded_per_quarter(self):
        five_years_ago = datetime.date.today() - datetime.timedelta(days=5*365)

        companies_per_quarter = (
            self.annotate(
                quarter=TruncQuarter('date_founded'),
                year=ExtractYear('date_founded')
            )
            .filter(date_founded__gte=five_years_ago)
            .values('quarter', 'year')
            .annotate(count=Count('id'))
            .order_by('-year', '-quarter')
        )

        return companies_per_quarter


class CompanyManager(models.Manager):
    def get_queryset(self):
        return CompanyQuerySet(self.model, using=self._db)

    def most_recently_founded(self, limit=10):
        return self.get_queryset().most_recently_founded(limit)

    def avg_employee_count(self):
        return self.get_queryset().avg_employee_count()

    def user_with_most_companies(self):
        return self.get_queryset().user_with_most_companies()

    def companies_founded_per_quarter(self):
        return self.get_queryset().companies_founded_per_quarter()


class EmployeeManager(models.Manager):
    def user_with_most_employees(self):
        return self.values('company__creator').annotate(total_employees=Sum('id')).order_by('-total_employees').first()['company__creator']


class DealManager(models.Manager):
    def avg_deals_amounts_by_country(self):
        return self.values('company__country__name').annotate(avg_amount_raised=Avg('amount_raised')).order_by('-avg_amount_raised').values('company__country__name', 'avg_amount_raised')
