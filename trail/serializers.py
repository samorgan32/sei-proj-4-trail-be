from rest_framework import serializers
from .models import Walkthrough, Slide

class WalkthroughSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(
        source = 'users.User',
        read_only = True
    )

    slides = serializers.StringRelatedField(
        many = True,
        read_only = True
    )

    class Meta:
        model = Walkthrough
        fields = ('id', 'title', 'owner', 'date_created', 'cover_slide', 'slides')


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ('id', 'title', 'image', 'description', 'walkthrough', 'position')
