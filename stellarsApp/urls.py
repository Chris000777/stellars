from django.urls import path

# -------------------- Vistas a importar -------------------- #
from stellarsApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('lounges', views.lounges, name="Salas"),
    path('promotions', views.promotions, name="Promociones"),
    path('previews/<int:id>', views.previews, name="Preestrenos"),    
    path('blog/', views.blog, name="Blog"),
    path('base', views.base, name="Base"),

    path('administracion/', views.base_admin,name='inicio_administracion'),
    path('administracion/posts', views.post,name='Posts'),
    path('administracion/posts/nuevo', views.post_nuevo,name='Post_nuevo'),
    path('administracion/posts/editar/<int:id_post>', views.post_editar,name='post_editar'),
    path('administracion/posts/eliminar/<int:id_post>', views.post_eliminar,name='post_eliminar'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
