from django.urls import path

from user import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('forgot', views.forget, name='forgot'),
    path('Register', views.register, name='Register'),
]