from django.conf.urls import patterns, url
# from rest_framework.urlpatterns import format_suffix_patterns
from vehicle.views import VehicleLocation, GetTestData
 
urlpatterns = patterns('',
  url(r'^location/$', VehicleLocation.as_view()),
  url(r'^testdata/$', GetTestData.as_view()),
)

# urlpatterns = format_suffix_patterns(urlpatterns)