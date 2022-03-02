from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='admin/login.html',
        redirect_authenticated_user=True,
        #authentication_form=forms.LoginForm,
        extra_context={'title': 'Log-in'}
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),

    path('', login_required(views.HomeView.as_view()), name='home'),
    
]