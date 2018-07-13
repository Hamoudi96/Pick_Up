# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    player = models.OneToOneField(User, default=0)

class Field(models.Model):
    field_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default='')
    

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=30)
    zip = models.IntegerField()
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    
    
class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=30)
    max = models.IntegerField()
    
    
class FieldLocation(models.Model):
    field_location = models.AutoField(primary_key=True)
    address_id = models.ForeignKey(Address,verbose_name="the address player", db_index=True)
    field_id = models.ForeignKey(Field,verbose_name="the field player", db_index=True)
    is_reserved = models.BooleanField(default=False)
    reservation_time = models.CharField(max_length=20)

    
class TeamPlayer(models.Model):
    team_player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey(Team, verbose_name="the related team", db_index=True)
    player_id = models.ForeignKey(Player, verbose_name="the related player", db_index=True)
    
    
class TeamAddress(models.Model):
    team_address_id = models.AutoField(primary_key=True)
    address_id = models.ForeignKey(Address, verbose_name="the related player", db_index=True)
    team_id = models.ForeignKey(Team, verbose_name="the related team", db_index=True)
    
    
