from django.urls import path
from account import views

from django.contrib.auth import views as authViews


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('resetPassword/',
         authViews.PasswordResetView.as_view(template_name='passwordReset.html'),
         name='reset_password'),
    path('resetPasswordSent/',
         authViews.PasswordResetDoneView.as_view(template_name='passwordResetSent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(template_name='passwordResetForm.html'),
         name='password_reset_confirm'),
    path('resetPasswordComplete/',
         authViews.PasswordResetCompleteView.as_view(template_name='passwordResetComplete.html'),
         name='password_reset_complete')
]
