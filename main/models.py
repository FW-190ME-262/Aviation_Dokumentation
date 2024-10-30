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
    courses = models.ManyToManyField('Course', related_name='students', blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)  # Добавлено поле баланса

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
    plane_type = models.CharField(max_length=255)
    complexity_level = models.CharField(max_length=255)
    download_link = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Добавлено поле стоимости


class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField()  # Ссылка на видеоурок
    created_at = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_publication = models.DateTimeField(auto_now_add=True)

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


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    video_url = models.URLField()
    date_publication = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey('Course', related_name='lessons', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class EducationalMaterial(models.Model):
    name = models.CharField(max_length=250)
    number_educational = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials')
    content = models.TextField()
    file = models.FileField(upload_to='educational_materials/', blank=True, null=True)

    def __str__(self):
        return self.name


"переходя подробно в курс я получаю список уроков , весь ма териал на список уроков"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.plane.name} in cart of {self.user.username}'


class CommentSerializer:
    class Meta:
        model = Plane
        fields = ['comment']


class RatingSerializer:
    class Meta:
        model = Plane
        fields = ['rating']


'напомнить Андрею заехать в Вайлберес и спросить про платежку линки дыня  '
