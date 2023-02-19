from django.db import models
from ckeditor import fields
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
     CITY = (
          ('NKS', 'Нукус'),
          ('TASH', 'Ташкент'),
     )

     first_name = models.CharField('Имя*', max_length=512)
     last_name = models.CharField('Фамилия*', max_length=512)
     email = models.EmailField('Эл.почта*')

     address = models.CharField('Адрес', max_length=5096)
     postcode = models.IntegerField('Почтовый индекс*', default=230119)
     city = models.CharField('Город', choices=CITY, max_length=512)

     phone = models.CharField('Телефон*', max_length=75)


     def __str__(self) -> str:
          return self.first_name
     
     class Meta:
          verbose_name = 'Покупатель'
          verbose_name_plural = 'Покупатели'


#P*Q5!8a!sK4cAzy