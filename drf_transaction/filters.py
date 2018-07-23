from django_filters import FilterSet


class RangeFiltering(FilterSet):
    """
    A filter class for applying filters.
    """
    from django_filters.rest_framework import NumberFilter, ModelMultipleChoiceFilter, CharFilter, DateFilter
    from .models import TransactionMode

    start_date = DateFilter(field_name='transaction_date', lookup_expr='gte')
    end_date = DateFilter(field_name='transaction_date', lookup_expr='lte')
    start_amount = NumberFilter(field_name='amount', lookup_expr='gte')
    end_amount = NumberFilter(field_name='amount', lookup_expr='lte')
    mode = ModelMultipleChoiceFilter(field_name='mode', queryset=TransactionMode.objects.all())
    amount = NumberFilter(field_name='amount')
    id = NumberFilter(field_name='id')
    category = CharFilter(field_name='category')
    transaction_date = DateFilter(field_name='transaction_date')

    class Meta:
        from .models import TransactionDetail

        model = TransactionDetail
        fields = ('start_date', 'end_date', 'start_amount', 'end_amount', 'mode', 'amount', 'id', 'category',
                  'transaction_date')
