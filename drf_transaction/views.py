from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response


class ShowTransactionAmount(ListAPIView):
    """
    This view is to show the details of transactions.
    """
    from .serializers import ShowTransactionDetailsSerializer
    from drfaddons.serializer import IsOwnerFilterBackend
    from django_filters.rest_framework import DjangoFilterBackend
    from rest_framework.filters import SearchFilter, OrderingFilter
    from .filters import RangeFiltering
    from .models import TransactionDetail

    queryset = TransactionDetail.objects.all().order_by('contact_id')
    serializer_class = ShowTransactionDetailsSerializer
    filter_backends = (IsOwnerFilterBackend, DjangoFilterBackend, SearchFilter, OrderingFilter)

    filter_class = RangeFiltering
    search_fields = ('^contact__name', )
    ordering_fields = ('contact__name', 'amount', 'transaction_date')

    def list(self, request, *args, **kwargs):
        from django.db.models import Sum

        queryset = self.filter_queryset(self.get_queryset())
        total = queryset.aggregate(Sum('amount'))
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
            paginated_response.data['total_amount'] = total['amount__sum']
            return paginated_response

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AddTransactionAmount(CreateAPIView):
    """
    This view is to add new transactions.
    """
    from .serializers import AddTransactionDetailsSerializer
    from rest_framework.parsers import JSONParser

    serializer_class = AddTransactionDetailsSerializer
    parser_classes = (JSONParser,)

    def perform_create(self, serializer):

        from drf_contact.models import ContactDetail

        contact_obj, create = ContactDetail.objects.get_or_create(name=serializer.validated_data['contact'],
                                                                  created_by=self.request.user)
        serializer.validated_data['contact'] = contact_obj
        serializer.save(created_by=self.request.user)


class DeleteTransactionAmount(DestroyAPIView):
    """
    This view is to delete a transaction.
    """
    from drfaddons.serializer import IsOwnerFilterBackend
    from .serializers import DeleteTransactionDetailsSerializer
    from .models import TransactionDetail

    filter_backends = (IsOwnerFilterBackend, )
    queryset = TransactionDetail.objects.all()
    serializer_class = DeleteTransactionDetailsSerializer


class UpdateTransactionAmount(UpdateAPIView):
    """
    This view is to update a transaction.
    """
    from .serializers import UpdateTransactionDetailsSerializer
    from drfaddons.serializer import IsOwnerFilterBackend
    from .models import TransactionDetail

    queryset = TransactionDetail.objects.all()
    serializer_class = UpdateTransactionDetailsSerializer
    filter_backends = (IsOwnerFilterBackend, )

    def perform_update(self, serializer):
        from drf_contact.models import ContactDetail

        if 'contact' in serializer.initial_data.keys():
            contact_obj, created = ContactDetail.objects.get_or_create(name=serializer.validated_data['contact'],
                                                                       created_by=self.request.user)
            serializer.validated_data['contact'] = contact_obj

        serializer.save(created_by=self.request.user)


class ShowMode(ListAPIView):
    """
    This view will show all the modes of transaction.
    """
    from .serializers import ShowModeSerializer
    from .models import TransactionMode
    from rest_framework.permissions import AllowAny

    permission_classes = (AllowAny, )
    queryset = TransactionMode.objects.all()
    serializer_class = ShowModeSerializer
    filter_backends = ()
