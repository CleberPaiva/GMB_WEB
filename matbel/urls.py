
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('unidade/', include('unidade.urls')),
    path('fornecedor/', include('fornecedor.urls')),
    path('pessoa/', include('pessoa.urls')),
    path('arma/', include('arma.urls')),
    path('mural/', include('mural.urls')),
    path('oficina/', include('oficina.urls')),
    path('material/', include('material.urls')),
    path('marca_arma/', include('marca_arma.urls')),
    path('marca_epi/', include('marca_epi.urls')),
    path('marca_municao/', include('marca_municao.urls')),
    path('servidor/', include('servidor.urls')),
    path('colete/', include('colete.urls')),
    path('gerencia/', include('gerencia.urls')),
    path('restricoes/', include('restricoes.urls')),
    path('cautela_unidade/', include('cautela_unidade.urls')),
    path('cautela_arma/', include('cautela_arma.urls')),
    path('cautela_material/', include('cautela_material.urls')),
    path('material_cautela/', include('material_cautela.urls')),
    path('arma_particular/', include('arma_particular.urls')),
    path('municao/', include('municao.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard_servidores/', include('dashboard_servidores.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
