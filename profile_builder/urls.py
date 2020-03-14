"""profile_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from profiles.views import FacultySearchList, bookmark_profile, BookmarksListView, faculty_info, \
    make_appointment, RequestsListView, accept_appointment, reject_appointment, \
    StatusRequestsListView, AppointmentListView
from users import views as user_views

urlpatterns = [
                  path('', FacultySearchList.as_view(), name='home'),
                  path('appointments/', AppointmentListView.as_view(), name='appointments'),
                  path('admin/', admin.site.urls),
                  path('register/', user_views.register, name='register'),
                  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
                  path('<int:pk>/favourite_post/', bookmark_profile, name='post-favourite'),
                  path('<int:pk>/faculty_info/', faculty_info, name='faculty-info'),
                  path('<int:pk>/accept_appointment/', accept_appointment, name='accept-appointment'),
                  path('<int:pk>/reject_appointment/', reject_appointment, name='reject-appointment'),
                  path('status-appointments/', StatusRequestsListView.as_view, name='status-appointment'),
                  path('bookmark/', BookmarksListView.as_view(), name='bookmarks'),
                  path('requests/', RequestsListView.as_view(), name='requests'),
                  path('profile/', user_views.profile, name='profile'),
                  path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
                  path('<int:pk>/make_appointment/', make_appointment, name='appointment'),
                  path('password-reset/',
                       auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
                       name='password_reset'),
                  path('password-reset/done/',
                       auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
                       name='password_reset_done'),
                  path('password-reset-confirm/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
                       name='password_reset_confirm'),
                  path('password-reset-complete/',
                       auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
                       name='password_reset_complete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
