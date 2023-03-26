from app.views import dadosViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', dadosViewSet)
urlpatterns = router.urls