from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views as quickviews
from routes import views as routeviews

router = routers.DefaultRouter()

# basic Django
router.register(r'users', routeviews.UserViewSet)
router.register(r'groups', quickviews.GroupViewSet)

# GoEco!
# user
router.register(r'ecouser', routeviews.EcoUserViewSet)
router.register(r'usersettings', routeviews.UserSettingsViewSet)
# date
router.register(r'weeks', routeviews.WeekViewSet)
router.register(r'days', routeviews.DayViewSet)
# routes
router.register(r'routes', routeviews.RouteViewSet)
router.register(r'reasons', routeviews.ReasonViewSet)
router.register(r'activities', routeviews.ActivityViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
