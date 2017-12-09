# -*- encoding: utf-8 -*-

import gae_storage
import bluemix_storage
import urllib
from django.conf import settings


def save(file_content, file_name, content_type):
    url1 = gae_storage.upload_file(file_content, file_name, content_type)
    url2 = bluemix_storage.upload_file(file_content, file_name, content_type)
    if url1:
        return url1
    else:
        return url2

def delete(file_name):
    r1 = gae_storage.delete_file(file_name)
    r2 = bluemix_storage.delete_file(file_name)
    if r1:
        return r1
    else:
        return r2


def retrieve(file_name):
    r = gae_storage.retrieve_file(file_name)
    if not r:
        r = bluemix_storage.retrieve_file(file_name)
    return r


def get_url(file_name):
    gs_base_url = settings.GS_BASE_URL
    bl_base_url = settings.BL_BASE_URL

    if url_exists(gs_base_url, file_name):
        return gs_base_url + file_name
    elif url_exists(bl_base_url, file_name):
        return bl_base_url + file_name
    else:
        return None


def url_exists(site, path):
    return urllib.urlopen(site + path).getcode() == 200
