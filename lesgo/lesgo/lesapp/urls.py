from django.urls import path
from lesapp import views

app_name='lesapp'

urlpatterns=[
    path('reg/',views.register,name='reg'),
    path('user_login/',views.user_login,name="user_login"),
]
