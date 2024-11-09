from .models import Plane, Comment, Rating, Tutorial
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Country, CityVillage, Region, District, Course, Lesson, EducationalMaterial, CartItem


# Сериализатор пользователя для работы с данными пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}  # Поле пароля доступно только для записи (безопасность)

    # Создание пользователя с хешированным паролем
    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


# Сериализатор регистрации нового пользователя с данными профиля
class RegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Вложенный сериализатор для данных пользователя

    class Meta:
        model = Profile
        fields = '__all__'

    # Создание профиля с привязкой к новому пользователю
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Создание профиля, связанного с пользователем
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


# Сериализатор для модели Country (страна)
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


# Сериализатор для модели Region (регион)
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


# Сериализатор для модели District (область)
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


# Сериализатор для модели CityVillage (город или село)
class CityVillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityVillage
        fields = '__all__'


# Сериализатор для добавления и просмотра комментариев к самолетам
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'user']  # Включает текст комментария и пользователя, оставившего его


# Сериализатор для оценки самолета
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rating', 'user']  # Включает значение рейтинга и пользователя, оценившего самолет


# Сериализатор для руководства (туториала)
class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['id', 'title', 'description', 'video_url', 'created_at']


# Сериализатор для элемента корзины
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'plane', 'quantity']  # Включает пользователя, модель самолета и количество


# Сериализатор для краткого отображения уроков в курсе
class LessonCourseDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title']  # Только ID и название урока


# Сериализатор для модели Course (курс)
class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonCourseDeteilSerializer(many=True, read_only=True)  # Вложенные данные о уроках

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'price', 'date_publication', 'lessons']


# Сериализатор для учебного материала
class EducationalMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalMaterial
        fields = ['id', 'name', 'number_educational', 'content', 'file']


# Сериализатор для урока с материалами
class LessonSerializer(serializers.ModelSerializer):
    materials = EducationalMaterialSerializer(many=True, read_only=True)  # Вложенные данные о материалах

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'content', 'video_url', 'date_publication', 'materials']


# Сериализатор для модели самолета Plane
class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['id', 'name', 'photo', 'description', 'text', 'date_publications', 'plan', 'plane_type',
                  'complexity_level', 'download_link', 'price']  # Добавлено поле price
