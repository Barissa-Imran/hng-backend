from rest_framework import serializers
from server.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['slackUsername', 'backend', 'age', 'bio']

    def create(self, validated_data):
        """
        create and return a new `Profile` instance, given validated data.
        """
        return Profile.objects.create(**validated_data)
