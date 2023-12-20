from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuItemSerializer, UserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Booking, MenuItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenuItemsView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 

