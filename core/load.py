from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Municipal

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

mun_shp = str(Path(__file__).resolve().parent / 'data' /
              'Tikapur_Municipal_Boundary.shp')


def mun(verbose=True):
    lm = LayerMapping(Municipal, mun_shp, municipal_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
