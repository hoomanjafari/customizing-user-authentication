from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None):
        if not email:
            raise ValueError('You have to type a email address')

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None):
        user = self.create_user(
            email,
            password=password,
            phone_number=phone_number
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    email = models.EmailField(unique=True,)
    phone_number = models.PositiveIntegerField(unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.email} --- {self.phone_number}'

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
