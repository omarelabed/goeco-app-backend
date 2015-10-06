from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views as quickviews
from routes import views as routeviews

router = routers.DefaultRouter()
router.register(r'users', quickviews.UserViewSet)
router.register(r'groups', quickviews.GroupViewSet)
router.register(r'routes', routeviews.RouteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
