from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Authentication
    path('users/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Menu
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
