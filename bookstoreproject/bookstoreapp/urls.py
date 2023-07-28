from django.urls import path

from bookstoreproject import settings
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path('', views.demo, name='demo'),
    path('index/', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)