from django.contrib import admin
from django.urls import path, include  # O'ZGARISH: views o'rniga include import qilindi, chunki dashboard.urls ni ulash uchun kerak
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  # O'ZGARISH: views('dashboard.urls') o'rniga include('dashboard.urls') ishlatildi, chunki bu dashboard ilovasining urls.py faylini ulaydi
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.contrib import admin
# from django.urls import path, views
# from django.conf import settings
# from django.conf.urls.static import static
# from users import views as user_views
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views('dashboard.urls')),
#     path('register/', user_views.register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
#     path('profile/', user_views.profile, name='profile'),
# ]

# # Serve media files in development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
