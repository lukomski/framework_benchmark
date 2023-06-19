from rest_framework import viewsets
from fwbm.models import Collision
from fwbm.serializers import CollisionSerializer

class CollisionView(viewsets.ModelViewSet):
    queryset = Collision.objects.all()
    serializer_class = CollisionSerializer