"""
URL configuration for tutorial_project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from tutorial_registration import views as user_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutorial_app_name1.urls')),
    path('register/', user_view.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='tutorial_registration/login.html'), name="login"),
    path('logout/', user_view.logout_view, name='logout'),
    path('about/', include('tutorial_app_name1.urls')),
    path('profile/',user_view.profile , name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)