from django.urls import path

# -------------------- Vistas a importar -------------------- #
from stellarsApp import views


urlpatterns = [
    path('', views.home, name="Inicio"),
    path('lounges', views.lounges, name="Salas"),
    path('promotions', views.promotions, name="Promociones"),
    path('previews', views.previews, name="Preestrenos"),
    path('blog/', views.blog, name="Blog"),
    path('base', views.base, name="Base"),
]
