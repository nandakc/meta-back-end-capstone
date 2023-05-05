from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from . import models, serializers

def index(request):
    return render(request, 'index.html', {})

def default_permissions(self):
    permission_classes = []          # anyone can see Menu items
    if self.request.method != 'GET': # only authenticated users can add, edit or delete menu item(s)
        permission_classes = [permissions.IsAuthenticated]
    return [permission() for permission in permission_classes]

class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    def get_permissions(self):
        return default_permissions(self)

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    def get_permissions(self):
        return default_permissions(self)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        permission_classes = []           # anyone can create Booking
        if self.request.method != 'POST': # only authenticated users can see, edit or delete a booking
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

