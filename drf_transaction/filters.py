from django_filters import FilterSet


class RangeFiltering(FilterSet):
    """
    A filter class for applying filters.
    """
    from django_filters.rest_framework import NumberFilter, ModelMultipleChoiceFilter, CharFilter, DateFilter
    from .models import TransactionMode

    start_date = DateFilter(name='transaction_date', lookup_expr='gte')
    end_date = DateFilter(name='transaction_date', lookup_expr='lte')
    start_amount = NumberFilter(name='amount', lookup_expr='gte')
    end_amount = NumberFilter(name='amount', lookup_expr='lte')
    mode = ModelMultipleChoiceFilter(name='mode', queryset=TransactionMode.objects.all())
    amount = NumberFilter(name='amount')
    id = NumberFilter(name='id')
    category = CharFilter(name='category')
    transaction_date = DateFilter(name='transaction_date')

    class Meta:
        from .models import TransactionDetail

        model = TransactionDetail
        fields = ('start_date', 'end_date', 'start_amount', 'end_amount', 'mode', 'amount', 'id', 'category',
                  'transaction_date')
