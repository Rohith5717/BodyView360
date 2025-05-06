from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('admin-dashboard/', views.admin_dashboard),
    path('viewer/', views.viewer),
    path('timeline/', views.health_timeline, name='timeline'),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Make sure this exists
    path('accounts/', include('django.contrib.auth.urls')),  # Optional
    # Add other app routes here
]
