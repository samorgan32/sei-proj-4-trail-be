from rest_framework import serializers
from .models import Walkthrough, Slide

class SlideSerializer(serializers.ModelSerializer):
    walkthrough = serializers.SlugRelatedField(
        queryset = Walkthrough.objects.all(),
        slug_field='pk'
    )

    walkthrough_owner = serializers.ReadOnlyField(source='walkthrough.owner.username')

    class Meta:
        model = Slide
        fields = ('id', 'image', 'description', 'walkthrough', 'position', 'walkthrough_owner')

class WalkthroughSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(
        source = 'users.User',
        read_only = True
    )

    slides = SlideSerializer(many=True, read_only=True)

    class Meta:
        model = Walkthrough
        fields = ('id', 'title', 'owner', 'date_created', 'cover_slide', 'slides')



