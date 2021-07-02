from django.shortcuts import render 
from rest_framework import viewsets
from .models import Walkthrough, Slide 
from .serializers import WalkthroughSerializer, SlideSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class WalkthroughViewSet(viewsets.ModelViewSet):
    queryset = Walkthrough.objects.all()
    serializer_class = WalkthroughSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Walkthrough.objects.all().filter(owner = self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



# class WalkthroughList(generics.ListCreateAPIView):
#     queryset = Walkthrough.objects.all()
#     serializer_class = WalkthroughSerializer

# class WalkthroughDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Walkthrough.objects.all()
#     serializer_class = WalkthroughSerializer

# class SlideList(generics.ListCreateAPIView):
#     queryset = Slide.objects.all()
#     serializer_class = SlideSerializer

# class SlideDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Slide.objects.all()
#     serializer_class = SlideSerializer



