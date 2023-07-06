from django.urls import path
from . import views
from django.conf import settings
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('login', auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='userregistration'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset-confirm.html', form_class=MySetPasswordForm), name='password_reset-confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset-complete.html'), name='password_reset-confirm'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='changepassword.html', form_class=MyPasswordChangeForm, success_url='passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('feedback/', views.feedback, name='feedback')
]