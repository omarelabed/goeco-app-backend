from django.contrib.auth.models import User
from django.db import models

# DEFAULT_REASON = 0


class UserSettings(models.Model):
    notifications = models.BooleanField()
    car_owner = models.BooleanField(default=False)


class GoEcoAccount(models.Model):
    """
    A *GoEco!* account can include all the data related to a user.
    """
    # #IDSIA
    # {
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
    #     "userId":"userId1",
    # TODO
    #     "username":"pinco pallino",
    # username = models.CharField(max_length=200)
    # --> already provided by user (see above)

    #     "weeks":[ ... ] --> fk in week
    # }
    # /IDSIA
    user_settings = models.OneToOneField(UserSettings, blank=True, null=True, on_delete=models.SET_NULL)
    # usersettings = EmbeddedModelField('UserSettings')


class Week(models.Model):
    """
    Week model is used to group the Route instances in weeks. This was created for the frontend.
    """
    goeco_account = models.ForeignKey(GoEcoAccount)
    # #IDSIA
    # {
    #     "weekId":"weekId1",
    # TODO
    #     "name":"Week 1",
    name = models.CharField(max_length=200)
    #     "validated":false,
    validated = models.BooleanField()
    # },
    # /IDSIA


class Reason(models.Model):
    """
    A set of reasons for the routes. Each route has one reason.
    """
    description = models.CharField(max_length=200)
    label = models.CharField(max_length=200)


class Route(models.Model):
    """
    This is the Route model provided by IDSIA with additional fields (i.e. week, reason, etc.)
    """
    week = models.ForeignKey(Week, blank=True, null=True, on_delete=models.SET_NULL)
    reason = models.ForeignKey(Reason, null=True)
    # #LOCAL
    # id

    # user_id
    user = models.ForeignKey(User, null=True)
    # /LOCAL

    # #IDSIA
    # {
    #     "startTime":"20121212T071430+0200",
    startTime = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    #     "endTime":"20121212T074617+0200",
    endTime = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    #     "co2":20,
    co2 = models.PositiveIntegerField(blank=True, null=True)
    #     "energy":10,
    energy = models.PositiveIntegerField(blank=True, null=True)
    #     "activities":[ ... ] --> fk in Activity
    # }
    # /IDSIA


class RouteAlternative(models.Model):
    """
    Similar to Route, but suggested as an alternative related to an existing route
    """
    route = models.OneToOneField(Route, blank=True, null=True, on_delete=models.SET_NULL)
    week = models.ForeignKey(Week, blank=True, null=True, on_delete=models.SET_NULL)
    reason = models.ForeignKey(Reason, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    startTime = models.DateTimeField(blank=True, null=True)
    endTime = models.DateTimeField(blank=True, null=True)
    co2 = models.PositiveIntegerField(blank=True, null=True)
    energy = models.PositiveIntegerField(blank=True, null=True)


class Activity(models.Model):
    """
    Sub-segment of a Route. This is related to an activity happening during a route/move.
    E.g. taking the bus or walking from A to B
    """
    route = models.ForeignKey(Route)

    # #IDSIA
    # {
    #     "activityMoves":"walking",
    activityMoves = models.CharField(max_length=200)
    #     "activityIDSIA":"walking",
    activityIDSIA = models.CharField(max_length=200)
    #     "activity":"walking",
    activity = models.CharField(max_length=200)
    #     "validated":true,
    validated = models.BooleanField()
    #     "startTime":"20121212T071430+0200",
    startTime = models.DateTimeField(blank=True, null=True)
    #     "endTime":"20121212T072732+0200",
    endTime = models.DateTimeField(blank=True, null=True)
    #     "duration":782,
    duration = models.IntegerField(blank=True, null=True)
    #     "distance":1251,
    distance = models.IntegerField(blank=True, null=True)
    #     "trackPoints":[ ... ] --> fk in trackpoint
    # },
    # /IDSIA


class TrackPoint(models.Model):
    """
    Sub-segment of an Activity with geographical information.
    """
    activity = models.ForeignKey(Activity)
    # #IDSIA
    # {
    #     "lat":55.55555,
    lat = models.FloatField()
    #     "lon":33.33333,
    lon = models.FloatField()
    #     "time":"20121212T071430+0200"
    time = models.DateTimeField()
    # },
    # /IDSIA
