from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
       def crear_usuario(self, email, password=None, **extra_fields):
              if not email:
                     raise ValueError("El usuario debe tener correo electrónico válido.")
              email = self.normalize_email(email)
              
              usuario = CustomUser(email=email, **extra_fields)
              usuario.set_password(password)
              usuario.save(using=self._db)
              
              return usuario
              
       def crear_superusuario(self, email, password=None, **extra_fields):
              extra_fields.setdefault('is_staff', True)
              extra_fields.setdefault('is_superuser', True)
              
              return self.crear_superusuario(email, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
       email = models.EmailField(unique=True)
       nombres = models.CharField(max_length=30)
       apellidos = models.CharField(max_length=30)
       is_active = models.BooleanField(default=True)
       is_staff = models.BooleanField(default=False)
       
       objects = CustomUserManager()
       
       USERNAME_FIELD = 'email'
       REQUIRED_FIELDS = ['nombres', 'apellidos']
       
       def __str__(self):
              return self.email