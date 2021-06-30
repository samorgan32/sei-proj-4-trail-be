from rest_framework import serializers
from .models import Walkthrough, Slide

class WalkthroughSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(
        source = 'users.User',
        read_only = True
    )

    Slides = serializers.StringRelatedField(
        source = 'slides',
        many = True,
        read_only = True
    )

    class Meta:
        model = Walkthrough
        fields = ('id', 'title', 'creator', 'date_created', 'cover_slide', 'Slides')


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ('id', 'title', 'images', 'description', 'walkthrough')
