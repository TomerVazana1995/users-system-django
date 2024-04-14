from django.urls import path
from .views import *

urlpatterns = [
    path('users/', user_list),
    path('users/<int:id>', user_detail),
    path('login/', login_user)
]