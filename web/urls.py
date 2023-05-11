from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    "birthday-celebrants", views.BirthdatCelebrantAPI, basename="birthday_celebrants"
)
router.register("sportlight", views.SpotLightAPI, basename="spotlight")
router.register("executives", views.ExecutiveAPI, basename="spotexecutiveslight")


urlpatterns = [
    path("", include(router.urls)),
]
