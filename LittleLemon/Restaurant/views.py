from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from . import models, serializers

def index(request):
    return render(request, 'index.html', {})

def default_permissions(self):
    permission_classes = []
    if self.request.method != 'GET':
        permission_classes = [permissions.IsAdminUser]

    return [permission() for permission in permission_classes]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.menu.objects.all()
    serializer_class = serializers.MenuSerializer
    def get_permissions(self):
        return default_permissions(self)

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.menu.objects.all()
    serializer_class = serializers.MenuSerializer
    def get_permissions(self):
        return default_permissions(self)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
