from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('homepage.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('profile/', include('profiles.urls')),
    path('checkout/', include('checkout.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'csan.views.handler404'
