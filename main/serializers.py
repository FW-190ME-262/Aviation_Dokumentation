from .models import Plane, Comment, Rating, Tutorial
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Country, CityVillage, Region, District
from .models import Course, Lesson, EducationalMaterial
from .models import CartItem


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


# class PlaneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Plane
#         fields = ['name', 'photo', 'description', 'text', 'date_publications']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'user', ]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'user', ]


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'description', 'video_url', 'created_at']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'plane', 'quantity']


class LessonCourseDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title']


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonCourseDeteilSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'price', 'date_publication', "lessons"]


class EducationalMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalMaterial
        fields = ['id', 'name', 'number_educational', 'content', 'file']


class LessonSerializer(serializers.ModelSerializer):
    materials = EducationalMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'content', 'video_url', 'date_publication', 'materials']


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['id', 'name', 'photo', 'description', 'text', 'date_publications', 'plan', 'plane_type',
                  'complexity_level', 'download_link', 'price']  # Добавлено поле price

