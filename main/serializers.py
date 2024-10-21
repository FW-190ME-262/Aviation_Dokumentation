from .models import Plane,Profile
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Country,CityVillage,Region,District


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class RegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        profile = Profile.objects.create(
            user=user,
            phone_number=validated_data['phone_number'],
            country=validated_data['country'],
            region=validated_data['region'],
            district=validated_data['district'],
            city_village=validated_data['city_village'],
            street=validated_data['street']
        )
        return profile


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class CityVillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityVillage
        fields = '__all__'


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['name', 'photo', 'description', 'text', 'date_publications']


class CommentSerializer:
    class Meta:
        model = Plane
        fields = ['comment']


class RatingSerializer:
    class Meta:
        model = Plane
        fields = ['rating']