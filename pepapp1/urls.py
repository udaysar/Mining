from django.urls import path 
from pepapp1 import views 

urlpatterns=[
    path('stocks/',views.stocks_list, name="stocks_list"),
    path('stocks/create/',views.stocks_create,name='stock_create'),
    path('stocks/<int:pk>/',views.stocks_detail,name='stock_detail'),
    path('stocks/<int:pk>/update/',views.stocks_update,name='stock_update'),
    path('stocks/<int:pk>delete/',views.stocks_delete,name='stock_delete'),
] 