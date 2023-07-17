# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_id, email, password, **extra_fields):
        if not user_id:
            raise ValueError("ID를 입력해주세요.")
        user_id = self.model.normalize_username(user_id)
        user = self.model(user_id=user_id, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, user_id, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(user_id, password, email, **extra_fields)

    def create_superuser(self, user_id, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff=True일 필요가 있습니다.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser=True일 필요가 있습니다.")
        return self._create_user(user_id, email, password, **extra_fields)


class User(AbstractBaseUser):
    # 아이디
    user_id = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=100, unique=True, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["email"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Buy(models.Model):
    num = models.AutoField(primary_key=True)
    mem = models.ForeignKey("Member", models.DO_NOTHING)
    prod_name = models.CharField(max_length=6, null=True)
    group_name = models.CharField(max_length=4, blank=True, null=True)
    price = models.IntegerField()
    amount = models.SmallIntegerField()


class Member(models.Model):
    mem_id = models.CharField(primary_key=True, max_length=8)
    mem_name = models.CharField(max_length=10)
    mem_number = models.IntegerField()
    addr = models.CharField(max_length=2)
    phone1 = models.CharField(max_length=3, blank=True, null=True)
    phone2 = models.CharField(max_length=8, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    debut_date = models.DateField(blank=True, null=True)
