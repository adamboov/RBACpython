from django.db import models
import datetime


# Create your models here.

class UserInfo(models.Model):
    ID = models.IntegerField(primary_key=True)
    UserName = models.CharField(max_length=32)
    RealName = models.CharField(max_length=32)
    PassWord = models.CharField(max_length=32)
    PhoneNumber = models.CharField(max_length=11)
    CreateTime = models.DateTimeField(default=datetime.datetime.now())
    LastLogin = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'UserInfo'


class Role(models.Model):
    ID = models.IntegerField(primary_key=True)
    RoleName = models.CharField(max_length=32)
    Description = models.CharField(max_length=128)

    class Meta:
        db_table = 'Role'


class Permission(models.Model):
    ID = models.IntegerField(primary_key=True)
    PermissionName = models.CharField(max_length=32)
    Description = models.CharField(max_length=128)
    Url = models.CharField(max_length=32)

    class Meta:
        db_table = 'Permission'


class PerToRole(models.Model):
    ID = models.IntegerField(primary_key=True)
    RoleId = models.IntegerField()
    PerId = models.IntegerField()

    class Meta:
        db_table = 'PerToRole'


class RoleToUser(models.Model):
    ID = models.IntegerField(primary_key=True)
    UserId = models.IntegerField()
    RoleId = models.IntegerField()

    class Meta:
        db_table = 'RoleToUser'
