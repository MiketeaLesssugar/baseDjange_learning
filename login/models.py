from django.db import models


# class UserAccountManager(BaseUserManager):
#
#     def create_user(self, email, first_name, last_name, password=None):
#         if not email:
#             raise ValueError('Users must have an email')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, first_name=first_name, last_name=last_name)
#         user.set_password(password)
#         user.save()
#
#         return user

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=30, verbose_name='用户名')
    password = models.CharField(max_length=16, verbose_name='用户密码')
    GENDER_CHOICES = (
        ('MALE', '男'),
        ('FEMALE', '女')
    )
    sex = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name='性别')
    age = models.CharField(max_length=6, verbose_name='年龄')
