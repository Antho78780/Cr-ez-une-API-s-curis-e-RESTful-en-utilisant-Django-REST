from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User, Contributor


class registerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"],
            password = validated_data["password"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ["user","project", "role"]