from django.urls import path

# -------------------- Vistas a importar -------------------- #
from stellarsApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('lounges', views.lounges, name="Salas"),
    path('promotions', views.promotions, name="Promociones"),
    path('previews', views.previews, name="Preestrenos"),
    path('blog/', views.blog, name="Blog"),
    path('base', views.base, name="Base"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
