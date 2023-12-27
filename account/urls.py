from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('', views.AccountView.as_view(), name='account'),
    path('account/edit/', views.AccountEditView.as_view(), name='account-edit'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
