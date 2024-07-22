from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_view, name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_don.html'), name='password_reset_don'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_conf.html'), name='password_reset_conf'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_compl.html'), name='password_reset_compl'),

    path('test-template/', views.test_template, name='test-template'),
]
