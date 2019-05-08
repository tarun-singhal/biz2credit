import django_filters
from .tables import table

class ProductFilter(django_filters.FilterSet):
    class Meta:
        # model = table
        fields = ['name', 'action', 'content']