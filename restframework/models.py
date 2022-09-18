# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Buy(models.Model):
    num = models.BigAutoField(primary_key=True)
    mem = models.ForeignKey('Member', models.DO_NOTHING)
    prod_name = models.CharField(max_length=6)
    group_name = models.CharField(max_length=4, blank=True, null=True)
    price = models.IntegerField()
    amount = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'buy'


class Member(models.Model):
    mem_id = models.CharField(primary_key=True, max_length=8)
    mem_name = models.CharField(max_length=10)
    mem_number = models.IntegerField()
    addr = models.CharField(max_length=2)
    phone1 = models.CharField(max_length=3, blank=True, null=True)
    phone2 = models.CharField(max_length=8, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    debut_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'
