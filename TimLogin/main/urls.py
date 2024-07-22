from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_view, name='logout'),

    path('create-quote/', views.create_quote, name="create_quote"),
    path('my-quote/', views.my_quotes, name="my_quotes"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_don.html'), name='password_reset_don'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_conf.html'), name='password_reset_conf'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_compl.html'), name='password_reset_compl'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_do.html'), name="password_change_do"),


    path('test-template/', views.test_template, name='test-template'),
]
