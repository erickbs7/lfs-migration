# -*- encoding: utf-8 -*-

# import swiftclient
import logging
import urllib2

from django.conf import settings
#from google.appengine.api import urlfetch
import requests

# def _get_connection():
#
#     try:
#         connection = swiftclient.Connection(
#             key=settings.BL_PASSWORD,
#             authurl=settings.BL_AUTH_URL,
#             auth_version=settings.BL_AUTH_VERSION,
#             os_options={
#                 "project_id": settings.BL_PROJECT_ID,
#                 "user_id": settings.BL_USER_ID,
#                 "region_name": settings.BL_REGION
#             }
#         )
#
#         return connection
#
#     except swiftclient.ClientException as e:
#         logging.debug('The connection withe bluemix failed.')
#         print(e)
#         return None


def upload_file(file_content, filename, content_type):
    # bluemix_connection = _get_connection()

    try:
        # result = urlfetch.fetch(
        #     url=settings.BL_BASE_URL + filename,
        #     payload=file_content,
        #     method=urlfetch.PUT,
        #     headers={'Content-Type': content_type, 'X-Auth-Token': settings.BL_AUTH_TOKEN})

        result = requests.put(settings.BL_BASE_URL + filename,
                  data=file_content,
                  headers={'Content-Type': content_type, 'X-Auth-Token': settings.BL_AUTH_TOKEN})

        if str(result) is '<Response [201]>':
            print('File {} uploaded to {} in Bluemix Object Storage.'.format(
                        filename,
                        filename))
            logging.debug('The upload for bluemix succeeded.')
            return True
        else:
            print(str(result))
            print('The upload of the file {} in {} failed in Bluemix Object Storage.'.format(
                        filename,
                        filename))
            logging.debug('The upload for bluemix failed.')
            return False

    except urllib2.URLError:
        logging.exception('Caught exception fetching url')

    # if bluemix_connection:
    #     try:
    #         bluemix_connection.put_object(
    #             settings.BL_CONTAINER_NAME,
    #             filename,
    #             contents=file_stream,
    #             content_type=content_type
    #         )
    #         logging.debug('The upload_file called for bluemix.')
    #         print('File {} uploaded to {} in Bluemix Object Storage.'.format(
    #             filename,
    #             filename))
    #         return True
    #     except Exception as e:
    #         print('The upload of the file {} in {} failed in Bluemix Object Storage.'.format(
    #             filename,
    #             filename))
    #         print(e)
    #         logging.debug('The upload for bluemix failed.')
    #         return False


def delete_file(filename):
    try:
        # result = urlfetch.fetch(
        #     url=settings.BL_BASE_URL + filename,
        #     method=urlfetch.DELETE,
        #     headers={'Content-Type': content_type,'X-Auth-Token': settings.BL_AUTH_TOKEN})
        #     headers={'X-Auth-Token': settings.BL_AUTH_TOKEN})

        result = requests.delete(settings.BL_BASE_URL + filename,
                                 headers={'X-Auth-Token': settings.BL_AUTH_TOKEN})

        if str(result) is '<Response [204]>':
            print('File {} deleted from {} in Bluemix Object Storage.'.format(
                        filename,
                        filename))
            logging.debug('The deletion for bluemix succeeded.')
            return True
        else:
            print('The deletion of the file {} in {} failed in Bluemix Object Storage.'.format(
                        filename,
                        filename))
            logging.debug('The deletion for bluemix failed.')
            return False

    except urllib2.URLError:
        logging.exception('Caught exception fetching url')

    # bluemix_connection = _get_connection()

    # if bluemix_connection:
    #     try:
    #         bluemix_connection.delete_object(settings.BL_CONTAINER_NAME, filename)
    #         print('File {} deleted in Bluemix Object Storage.'.format(filename))
    #         return True
    #     except swiftclient.ClientException as e:
    #         print('The file {} failed to be deleted in Bluemix Object Storage.'.format(filename))
    #         print(e)
    #         return False


def retrieve_file(filename):
    logging('retrieve_file from bluemix_storage called.')
    # bluemix_connection = _get_connection()

    # if bluemix_connection:
    #     try:
    #         return bluemix_connection.get_object(settings.BL_CONTAINER_NAME, filename)
    #     except swiftclient.ClientException as e:
    #         print('The file {} failed to be retried from Bluemix Object Storage.'.format(filename))
    #         print(e)
    #         return None
