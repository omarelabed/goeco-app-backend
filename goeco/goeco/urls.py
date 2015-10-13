from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views as quickviews
from routes import views as routeviews

router = routers.DefaultRouter()
# GoEco!
# user
router.register(r'goecoaccount', routeviews.GoEcoAccountViewSet)
router.register(r'usersettings', routeviews.UserSettingsViewSet)
# time grouping
router.register(r'weeks', routeviews.WeekViewSet)
# routes
router.register(r'routes', routeviews.RouteViewSet)
router.register(r'reasons', routeviews.ReasonViewSet)
router.register(r'activities', routeviews.ActivityViewSet)

# basic Django
router.register(r'users', routeviews.UserViewSet)
router.register(r'groups', routeviews.GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
