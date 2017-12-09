# -*- encoding: utf-8 -*-

import logging
import urllib2

from django.conf import settings
import requests


def upload_file(file_content, filename, content_type):

    try:
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

def delete_file(filename):
    try:
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

def retrieve_file(filename):
    logging('retrieve_file from bluemix_storage called.')