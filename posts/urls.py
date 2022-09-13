from django.urls import path
from .views import UserView, PostView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("users", UserView, basename="users")
router.register("", PostView, basename="Posts")

urlpatterns = router.urls
