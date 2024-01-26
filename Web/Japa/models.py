from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.files.base import ContentFile
import base64

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    address_type = models.CharField(max_length=20, choices=[('house', 'House'), ('apartment', 'Apartment'), ('office', 'Office'), ('other', 'Other')], blank=True, null=True)
    door_number = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class FoodType(models.Model):
    food_type = models.CharField(max_length=20, choices=[
        ('burger', 'Burger'),
        ('kebab', 'Kebab'),
        ('pizza', 'Pizza'),
        ('salat', 'Salat'),
        ('asiatisk', 'Asiatisk'),
        ('japansk', 'Japansk'),
        ('kinesisk', 'Kinesisk'),
        ('mexicansk', 'Mexicansk'),
        ('thai', 'Thai'),
        ('middelhavskøkken', 'Middelhavskøkken'),
        ('sandwich', 'Sandwich'),
        ('sushi', 'Sushi'),
        ('andet', 'Andet')
        ])
    
    def __str__(self):
        return self.food_type

class NewRestaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=50, default='Mad')
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    delivery_fee = models.FloatField()
    minimum_order = models.FloatField()
    FoodType = models.ManyToManyField('FoodType', related_name='FoodType')
    image = models.BinaryField(blank=True, null=True)

    def set_image(self, image):
        binary_data = image.read()
        self.image = binary_data

    def get_image(self):
        if self.image:
            return base64.b64encode(self.image).decode()
        else:
            return None
    

class NewCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.BinaryField(blank=True, null=True)

    def set_image(self, image):
        binary_data = image.read()
        self.image = binary_data
    
    def get_image(self):
        if self.image:
            return base64.b64encode(self.image).decode()
        else:
            return None