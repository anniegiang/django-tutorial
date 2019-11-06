from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
# Viewsets create a full CRUD api without having to explicitly specify methods for the functionality


class LeadViewSet(viewsets.ModelViewSet):
    #query that grabs all the leads
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
