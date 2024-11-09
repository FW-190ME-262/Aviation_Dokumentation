from django.db import models
from django.contrib.auth.models import User


# Модель страны
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название страны, уникальное для каждой записи

    def __str__(self):
        return self.name


# Модель региона, связанного с конкретной страной
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название региона
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='regions')  # Ссылка на страну

    def __str__(self):
        return f"{self.name}, {self.country.name}"


# Модель района, связанного с регионом
class District(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название района
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')  # Ссылка на регион

    def __str__(self):
        return f"{self.name}, {self.region.name}"


# Модель города или села, связанного с районом
class CityVillage(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название города или села
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='cities_villages')  # Ссылка на район

    def __str__(self):
        return f"{self.name}, {self.district.name}"


# Модель профиля пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # Связь с пользователем
    phone_number = models.CharField(max_length=15, unique=True)  # Уникальный номер телефона
    country = models.ForeignKey(Country, on_delete=models.CASCADE)  # Страна пользователя
    region = models.ForeignKey(Region, on_delete=models.CASCADE)  # Регион пользователя
    district = models.ForeignKey(District, on_delete=models.CASCADE)  # Район пользователя
    city_village = models.ForeignKey(CityVillage, on_delete=models.CASCADE)  # Город/село пользователя
    street = models.CharField(max_length=100)  # Улица проживания
    courses = models.ManyToManyField('Course', related_name='students',
                                     blank=True)  # Курсы, на которые записан пользователь
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)  # Баланс пользователя

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['country', 'region', 'district', 'city_village'],
                name='unique_location'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.city_village.name}, {self.street}"


# Модель самолета
class Plane(models.Model):
    name = models.CharField(max_length=255)  # Название самолета
    photo = models.ImageField(upload_to='planes/')  # Изображение самолета
    description = models.TextField()  # Краткое описание самолета
    text = models.TextField()  # Полное описание самолета
    date_publications = models.DateTimeField(auto_now_add=True)  # Дата публикации
    plan = models.ImageField(upload_to='plan/')  # Чертеж самолета
    plane_type = models.CharField(max_length=255)  # Тип самолета
    complexity_level = models.CharField(max_length=255)  # Уровень сложности
    download_link = models.URLField()  # Ссылка для скачивания
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Цена самолета


# Модель туториала
class Tutorial(models.Model):
    title = models.CharField(max_length=255)  # Название урока
    description = models.TextField()  # Описание урока
    video_url = models.URLField()  # Ссылка на видеоурок
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания


# Модель курса
class Course(models.Model):
    name = models.CharField(max_length=255)  # Название курса
    description = models.TextField()  # Описание курса
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость курса
    date_publication = models.DateTimeField(auto_now_add=True)  # Дата публикации курса

    def __str__(self):
        return self.name


# Модель комментария к самолету
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, оставивший комментарий
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)  # Самолет, к которому оставлен комментарий
    text = models.TextField()  # Текст комментария
    date_posted = models.DateTimeField(auto_now_add=True)  # Дата публикации комментария

    def __str__(self):
        return f'Comment by {self.user.username} on {self.plane.name}'


# Модель рейтинга самолета
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, оставивший рейтинг
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)  # Оцениваемый самолет
    score = models.IntegerField()  # Оценка от 1 до 10

    class Meta:
        unique_together = (
        'user', 'plane')  # Ограничение, чтобы пользователь мог оставить только одну оценку для самолета

    def __str__(self):
        return f'Rating by {self.user.username} for {self.plane.name}: {self.score}'


# Модель урока в курсе
class Lesson(models.Model):
    title = models.CharField(max_length=255)  # Название урока
    description = models.TextField()  # Описание урока
    content = models.TextField()  # Содержание урока
    video_url = models.URLField()  # Ссылка на видео
    date_publication = models.DateTimeField(auto_now_add=True)  # Дата публикации
    course = models.ForeignKey('Course', related_name='lessons',
                               on_delete=models.CASCADE)  # Курс, к которому принадлежит урок

    def __str__(self):
        return self.title


# Модель образовательного материала, привязанного к уроку
class EducationalMaterial(models.Model):
    name = models.CharField(max_length=250)  # Название материала
    number_educational = models.IntegerField()  # Порядковый номер материала
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               related_name='materials')  # Урок, к которому принадлежит материал
    content = models.TextField()  # Содержание материала
    file = models.FileField(upload_to='educational_materials/', blank=True, null=True)  # Файл материала (опционально)

    def __str__(self):
        return self.name


# Модель элемента корзины для покупки самолета
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, добавивший самолет в корзину
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)  # Самолет в корзине
    quantity = models.IntegerField(default=1)  # Количество самолета
    added_at = models.DateTimeField(auto_now_add=True)  # Дата добавления в корзину

    def __str__(self):
        return f'{self.plane.name} in cart of {self.user.username}'


# Модель инструкции по эксплуатации
class Instruction(models.Model):
    page = models.CharField(max_length=100)  # Название страницы или раздела инструкции
    text = models.TextField()  # Содержание инструкции

    def __str__(self):
        return f"Instruction for {self.page}"
