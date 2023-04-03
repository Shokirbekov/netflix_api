from film.views import *
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("kinolar", KinoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('hello/', HelloApiView.as_view()),
    path('aktors/', AktyorAPIView.as_view()),
    path('tarifs/', TarifAPIView.as_view()),
    path('aktor/<int:pk>/', AktyorDetailView.as_view()),
    path('izohlar/', IzohAPIView.as_view()),
    path('izoh_delete/<int:pk>/', IzohDeleteView.as_view()),
    # path('film/<int:pk>/', KinoDetailAPIView.as_view()),
]
