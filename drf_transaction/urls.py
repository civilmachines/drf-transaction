from django.urls import path
from . import views


app_name = 'drf_transaction'

urlpatterns = [
    # ex: api/transactions/add/
    path('add/', views.AddTransactionAmount.as_view(), name='Add-Transaction-Amount'),
    # ex: api/transactions/show/
    path('show/', views.ShowTransactionAmount.as_view(), name='Show-Transactions-Amount'),
    # ex: api/transactions/mode/show/
    path('mode/show/', views.ShowMode.as_view(), name='Show-Mode'),
    # ex: api/transactions/pk/delete/
    path('<int:pk>/delete/', views.DeleteTransactionAmount.as_view(), name='Delete-Transaction-Amount'),
    # ex: api/transactions/pk/update/
    path('<int:pk>/update/', views.UpdateTransactionAmount.as_view(), name='Update-Transaction-Amount'),
]
