from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),  # noqa
    path('favourites/', views.favourite_list, name='favourite'),
    path('favourite_add/<int:product_id>', views.favourite_add, name='favourite_add'),  # noqa
    path('favourite_list/<user_id>', views.favourite_list, name='favourite_list'),  # noqa
]

