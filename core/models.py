from django.contrib.gis.db import models


# Create your models here.
"""
Field Name Availabe in ShapeFile

FIRST_DIST
FIRST_GaPa
FIRST_Type
Sum_AREA
Sum_Househ
Sum_Total
Sum_Male
Sum_Female

geofield: MultiPolygon

"""


class Municipal(models.Model):
    first_dist = models.CharField(max_length=50)
    first_gapa = models.CharField(max_length=50)
    first_type = models.CharField(max_length=50)
    sum_area = models.FloatField()
    sum_househ = models.FloatField()
    sum_total = models.FloatField()
    sum_male = models.FloatField()
    sum_female = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.first_gapa

# python manage.py ogrinspect core/data/Tikapur_Municipal_Boundary.shp Municipal --srid=4326 --mapping --multi


"""

class Municipal(models.Model):
    first_dist = models.CharField(max_length=50)
    first_gapa = models.CharField(max_length=50)
    first_type = models.CharField(max_length=50)
    sum_area = models.FloatField()
    sum_househ = models.FloatField()
    sum_total = models.FloatField()
    sum_male = models.FloatField()
    sum_female = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for Municipal model
municipal_mapping = {
    'first_dist': 'FIRST_DIST',
    'first_gapa': 'FIRST_GaPa',
    'first_type': 'FIRST_Type',
    'sum_area': 'Sum_AREA',
    'sum_househ': 'Sum_Househ',
    'sum_total': 'Sum_Total',
    'sum_male': 'Sum_Male',
    'sum_female': 'Sum_Female',
    'geom': 'MULTIPOLYGON',
}


"""
