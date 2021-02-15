from django.urls import include, path
from account import views
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import views as authViews
from .views import *


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


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
         name='password_reset_complete'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login/', csrf_exempt(authViews.LoginView.as_view())),
    path('api/registation/', apiUserRegistration, name='apiRegistration')
]
