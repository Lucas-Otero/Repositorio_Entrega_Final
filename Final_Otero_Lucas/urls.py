from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('media/', include('media.urls')),
    path('accounts/', include('accounts.urls')),
    path('users/', include('users.urls')),
]
