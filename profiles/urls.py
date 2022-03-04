from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('favourite/<int:product_id>>', views.favourite_add, name='favourite_add'),
    path('profile/favourite', views.favourite_list, name='favourite_list')
]
