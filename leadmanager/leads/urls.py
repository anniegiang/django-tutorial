from rest_framework import routers
from .api import LeadViewSet #from api file bring in the viewset

router = routers.DefaultRouter()

#register an endpoint
router.register('api/leads', LeadViewSet, 'leads') # third arg is just a name

urlpatterns = router.urls # give urls that are registered for the 'api/leads' endpoint
