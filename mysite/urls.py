from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

path('robots.txt', TemplateView.as_view(template_name='static/robots.txt', content_type='text/plain')),