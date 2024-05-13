from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

# Феруза Фарм
# Калъcий хлор 5% - 100мл
# 1Чой кошикдан 3 махал хар куни
# 2024-05-12
# 2024-05-12
# 5000