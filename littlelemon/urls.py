
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet
from restaurant import views

router = DefaultRouter()

router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/',include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

# http://localhost:8000/restaurant/menu/   Shows menu items for
# http://localhost:8000/restaurant/booking/tables/
