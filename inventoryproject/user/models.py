from django.db import models
from django.contrib.auth.models import User
from PIL import *

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address =models.CharField(max_length=200, null=True, verbose_name='Direccion')
    phone= models.CharField(max_length=10, null=True, verbose_name='Telefono')
    image= models.ImageField(default='avatar.png', upload_to='profile_Images', verbose_name='Imagen')

    def __str__(self):
        return f'{self.staff.username}--Profile'