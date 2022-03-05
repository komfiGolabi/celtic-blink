from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),  # noqa
    path('favourite_add/<int:product_id>', views.favourite_add, name='favourite_add'),  # noqa
    path('favourite_list/<int:user_id>', views.favourite_list, name='favourite_list'),  # noqa
]
