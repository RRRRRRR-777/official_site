from django.views.generic import TemplateView

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('robots.txt', TemplateView.as_view(template_name='static/robots.txt', content_type='text/plain')),  # <- append
]