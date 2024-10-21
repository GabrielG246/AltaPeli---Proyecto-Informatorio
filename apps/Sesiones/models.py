from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, usuario, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(usuario=usuario, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(usuario, email, password, **extra_fields)

    def get_by_natural_key(self, usuario):
        return self.get(usuario=usuario)


class User(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=20, verbose_name=_('Nombre'))
    apellido = models.CharField(max_length=20, verbose_name=_('Apellido'))
    usuario = models.CharField(max_length=30, unique=True, verbose_name=_('Usuario'))
    email = models.EmailField(unique=True, verbose_name=_('Correo Electrónico'))
    password = models.CharField(max_length=128, verbose_name=_('Contraseña'))
    profile_image = models.ImageField(default='DefaultUser.png',upload_to='imagenes_perfil', blank=True, null=True, verbose_name=_('Imagen de perfil'))

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'email']

    def __str__(self):
        return self.nombre
