from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, id, name, email, sex, addr, access_key, secret_key, password=None):
        if not id:
            raise ValueError('user_id error')

        user = self.model(
            id=id,
            name=name,
            email=email,
            sex=sex,
            addr=addr,
            access_key=access_key,
            secret_key=secret_key
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, name, email, sex, addr, access_key, secret_key, password):
        user = self.create_user(
            id=id,
            password=password,
            name=name,
            email=email,
            sex=sex,
            addr=addr,
            access_key=access_key,
            secret_key=secret_key
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.CharField(
        verbose_name='아이디',
        max_length=32,
        unique=True,
        primary_key=True,
        null=False
    )
    password = models.CharField(max_length=128, null=False)
    date_of_birth = models.DateField(null=True)
    name = models.CharField(max_length=16, null=False)
    email = models.EmailField(max_length=128, unique=True, null=False)
    sex = models.CharField(max_length=10, null=False)
    addr = models.CharField(max_length=300, null=False)
    register_dttm = models.DateTimeField(auto_now_add=True)
    access_key = models.CharField(unique=True, null=True, max_length=200)
    secret_key = models.CharField(unique=True, null=True, max_length=200)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name', 'email', 'sex', 'addr', 'password', 'access_key', 'secret_key']

    def __str__(self):
        return self.id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
