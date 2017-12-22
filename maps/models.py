from django.db import models


class Map(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    author = models.CharField(max_length=50, blank=True)
    type = models.IntegerField()
    checkpoints = models.SmallIntegerField()
    bonuses = models.SmallIntegerField()
    difficulty = models.SmallIntegerField()
    prevent_prehop = models.SmallIntegerField()
    enable_baked_triggers = models.BooleanField()
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Spawn(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    zone = models.SmallIntegerField()
    type = models.SmallIntegerField()
    origin = models.CharField(max_length=80)
    angle = models.CharField(max_length=80)
    velocity = models.CharField(max_length=80)

    class Meta:
        unique_together = (('map', 'zone', 'type'),)


class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    start = models.CharField(max_length=80)
    end = models.CharField(max_length=80)
    type = models.IntegerField()
    value = models.IntegerField()
    limit_speed = models.BooleanField()
    target_name = models.CharField(max_length=32, blank=True)
    filter_name = models.CharField(max_length=32, blank=True)


class MapConfiguration(models.Model):
    map = models.OneToOneField(Map, primary_key=True, on_delete=models.CASCADE)
    config = models.CharField(max_length=20000, blank=True, null=True)