# -*- encoding: utf-8 -*-

from __future__ import absolute_import

from django.conf import settings
from google.cloud import storage
from google.cloud.exceptions import NotFound
import six

from io import BytesIO


def _get_blob(filename):
    client = storage.Client(project=settings.PROJECT_ID)
    bucket = client.bucket(settings.GS_BUCKET_NAME)
    return bucket.blob(filename)


def upload_file(file_content, filename, content_type):
    blob = _get_blob(filename)
    try:
        blob.upload_from_string(
            file_content.read(),
            content_type=content_type)
        print('File {} uploaded to {} in Google Cloud Storage.'.format(
            filename,
            filename))
    except Exception as e:
        print('The upload of the file {} in {} failed in Google Cloud Storage.'.format(
            filename,
            filename))
        print(e)
        return None

    url = blob.public_url

    if isinstance(url, six.binary_type):
        url = url.decode('utf-8')

    return url


def delete_file(filename):
    blob = _get_blob(filename)

    try:
        deleted_blob = blob.delete()
        if deleted_blob:
            print('File {} deleted in Google Cloud Storage.'.format(filename))
            return True
    except NotFound as e:
        print('The deletion of the File {} failed because was not found in Google Cloud Storage.'.format(filename))
        print(e)
        return False


def retrieve_file(filename):
    blob = _get_blob(filename)

    try:
        file_string = blob.download_as_string()
        return BytesIO(file_string)
    except NotFound as e:
        print('The file {} failed to be retried because was not found in Google Cloud Storage.'.format(filename))
        print(e)
        return None
