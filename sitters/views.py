from .models import Sitter
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SitterSerializer

class SitterViewSet(viewsets.ModelViewSet):
    queryset = Sitter.objects.all()
    serializer_class = SitterSerializer
    permission_classes = [permissions.AllowAny]