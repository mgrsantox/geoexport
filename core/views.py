from django.shortcuts import render
from core.models import Municipal
from django.core.serializers import serialize

# # import pandas as pd
import geopandas
# # import json
from django.http import HttpResponse


from django.utils.crypto import get_random_string
from django.conf import settings
import os
import shutil

import zipfile
import os

media_location = settings.MEDIA_ROOT


# def handle_uploaded_file(f, folder_name):
#     if not os.path.exists(media_location + '/' + folder_name + '/'):
#         os.makedirs(media_location + '/' + folder_name + '/')
#     with open(media_location + '/' + folder_name + '/' + f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def gen_location(folder_name):
    full_path = ''
    if not os.path.exists(media_location + '/' + folder_name + '/'):
        os.makedirs(media_location + '/' + folder_name + '/')
        full_path = media_location + '/' + folder_name + '/'
    return full_path


''' Zip files in folder news to testzip.zip  '''

folder_to_be_zipped = 'news'


def makezip(path, folder):
    with zipfile.ZipFile(folder + '.zip', 'w', zipfile.ZIP_DEFLATED) as newzip:
        for dirpath, dirnames, files in os.walk(folder_to_be_zipped):
            for file in files:
                newzip.write(os.path.join(path, file))


def make_archive(source, destination):
    base_name = '.'.join(destination.split('.')[:-1])
    format = destination.split('.')[-1]
    root_dir = os.path.dirname(source)
    base_dir = os.path.basename(source.strip(os.sep))
    shutil.make_archive(base_name, format, root_dir, base_dir)


def index(request):
    return render(request, 'index.html')


def to_shp(request):
    folder_name = get_random_string(length=15)
    print("!!! Start")
    data = Municipal.objects.filter(first_gapa="Tikapur")
    gd = serialize('geojson', data, geometry_field='geom',
                   fields=('first_dist', 'first_gapa'))
    df = geopandas.read_file(gd)
    location = gen_location(folder_name)
    df.to_file(location + "/Tikapur.shp")
    try:
        print("!!Zippppingggg!!")
    # makezip(location, folder_name)
    # make_archive(location, location)
        print("location is :" + location)
        kl = shutil.make_archive(
            root_dir=location, format='zip', base_name=location)
        print(kl)
    except Exception as e:
        print(e)
    file_loc = media_location + "/" + folder_name + ".zip"
    response = HttpResponse(
        open(file_loc, 'rb'), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=Municipal.zip'
    return response
    # zip_file = open(str(location), 'r')
    # print("zipfile location: " + zip_file)
    # response = HttpResponse(
    #     zip_file, content_type='application/force-download')
    # response['Content-Disposition'] = 'attachment; filename="%s"' % 'foo.zip'
    # return response
#     data = Municipal.objects.filter(first_gapa="Tikapur")
#     # df = pd.DataFrame(data)
#     # f = geopandas.GeoDataFrame(columns=[data])
#     # print(df.head())

#     gd = serialize('geojson', data, geometry_field='geom',
#                    fields=('first_dist', 'first_gapa'))
#     # gd1 = json.loads(gd)
#     # print(type(gd1))
#     df = geopandas.read_file(gd)
#     print(df)
#     k = df.to_file("/home/mgrsantox/Documents/certificate/Tikapur.shp")
#     folder_name = get_random_string(length=15)
#     handle_uploaded_file(_file, folder_name)
#     print(k)
#     return HttpResponse(k)


def to_geojson(request):
    data = Municipal.objects.filter(first_gapa="Tikapur")
    gd = serialize('geojson', data, geometry_field='geom',
                   fields=('first_dist', 'first_gapa'))

    response = HttpResponse(gd, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="result.json"'
    return response
