
from django.urls import path

from clinique import views
from integration import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.home,name="home")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
