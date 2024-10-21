from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='regions')

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return f"{self.name}, {self.region.name}"


class CityVillage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='cities_villages')

    def __str__(self):
        return f"{self.name}, {self.district.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city_village = models.ForeignKey(CityVillage, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['country', 'region', 'district', 'city_village'],
                name='unique_location'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.city_village.name}, {self.street}"


class Plane(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='planes/')
    description = models.TextField()
    text = models.TextField()
    date_publications = models.DateTimeField(auto_now_add=True)
    plan = models.ImageField(upload_to='plan/')

    # Поле для комментариев
    comments = models.ManyToManyField(User, through='Comment', related_name='plane_comments')

    # Поле для хранения оценок
    ratings = models.ManyToManyField(User, through='Rating', related_name='plane_ratings')

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.plane.name}'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    score = models.IntegerField()  # Оценка от 1 до 10

    class Meta:
        unique_together = ('user', 'plane')  # Каждый пользователь может оценить самолет только один раз

    def __str__(self):
        return f'Rating by {self.user.username} for {self.plane.name}: {self.score}'
