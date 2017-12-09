# -*- encoding: utf-8 -*-
from django.db import models

from lfs.cloud_storage import cloud_storage
from image_utils import generate_thumb


def get_thumbnails_string(sizes):
    sizes_list = []
    for size in sizes:
        sizes_list.append(str(size[0]) + 'x' + str(size[1]))
    return ','.join(sizes_list)


def parse_image(image_string):
    params_list = image_string.split(',')
    params_list_size = len(params_list)
    sizes_list = []

    if params_list_size == 2:
        return CloudImage(upload_to=params_list[0], file_name=params_list[1])

    elif params_list_size > 2:
        count = 2
        while count < params_list_size:
            sizes_list.append(tuple(map(int, params_list[count].split('x'))))
            count += 1

        return CloudImage(upload_to=params_list[0], file_name=params_list[1], sizes=tuple(sizes_list))

    else:
        print(params_list)
        print("Invalid input for a CloudImage instance.")
        return None


class CloudImage(object):
    def __init__(self, file_name=None, upload_to=None, sizes=None):
        self.file_name = file_name
        self.upload_to = upload_to
        self.sizes = sizes

    def __repr__(self):
        result_string = str(self.upload_to) + ',' + str(self.file_name)
        if self.sizes:
            result_string = result_string + ',' + get_thumbnails_string(self.sizes)
        return result_string

    def get_file_name(self):
        return self.upload_to + '/' + self.file_name

    def get_thumb_name(self, size):
        if self.sizes:
            if size in self.sizes:
                return self.upload_to + '/' + self.format_thumb_name(size)

        return None

    @property
    def url_60x60(self):
        if self.thumbnail_exist((60, 60)):
            return self.get_url((60, 60))
        else:
            return self.get_url()

    @property
    def url_100x100(self):
        if self.thumbnail_exist((100, 100)):
            return self.get_url((100, 100))
        else:
            return self.get_url()

    @property
    def url_200x200(self):
        if self.thumbnail_exist((200, 200)):
            return self.get_url((200, 200))
        else:
            return self.get_url()

    @property
    def url_400x400(self):
        if self.thumbnail_exist((400, 400)):
            return self.get_url((400, 400))
        else:
            return self.get_url()

    def format_thumb_name(self, size):
        if isinstance(size, tuple):
            (w, h) = size
            print("File Name: " + self.file_name)
            print("Upload to: " + self.upload_to)
            split = self.file_name.rsplit('.', 1)
            return '%s_%sx%s.%s' % (split[0], w, h, split[1])
        else:
            return None

    def thumbnail_exist(self, size):
        if self.sizes:
            return size in self.sizes
        else:
            return False

    def get_url(self, size=None):
        if size:
            return cloud_storage.get_url(self.get_thumb_name(size))
        else:
            return cloud_storage.get_url(self.get_file_name())

    def save(self, content, file_name, upload_to):
        self.file_name = file_name
        self.upload_to = upload_to

        url = cloud_storage.save(content, self.get_file_name(), content.content_type)

        if self.sizes:
            for size in self.sizes:
                split = self.file_name.rsplit('.', 1)
                thumb_name = self.upload_to + '/' + self.format_thumb_name(size)
                thumb_content = generate_thumb(content, size, split[1])
                print(thumb_content.content_type)
                # TODO: Grande possibilidade de gargalo. Tentar salvar em lotes.
                cloud_storage.save(thumb_content, thumb_name, thumb_content.content_type)

        return url

    def delete(self):
        if self.file_name is not None and self.upload_to is not None:
            cloud_storage.delete(self.upload_to + '/' + self.file_name)

            if self.sizes:
                for size in self.sizes:
                    thumb_name = self.upload_to + '/' + self.format_thumb_name(size)
                    cloud_storage.delete(thumb_name)
        else:
            raise Exception("Instance of Cloud Image was not initialized.")

    def retrieve(self):
        if self.file_name is not None and self.upload_to is not None:
            image = cloud_storage.retrieve(self.upload_to + '/' + self.file_name)
            return image
        else:
            raise Exception("Instance of Cloud Image was not initialized.")


class CloudImageField(models.Field):
    description = "A image storaded in a cloud service."

    def __init__(self, file_name=None, upload_to=None, sizes=None, *args, **kwargs):
        self.file_name = file_name
        self.upload_to = upload_to
        self.sizes = sizes
        super(CloudImageField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CloudImageField, self).deconstruct()
        if self.file_name is not None:
            kwargs['file_name'] = self.file_name
        if self.upload_to is not None:
            kwargs['upload_to'] = self.upload_to
        if self.sizes is not None:
            kwargs['sizes'] = self.sizes
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'char(200)'

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return parse_image(value)

    def to_python(self, value):
        if value is None:
            return value

        if isinstance(value, CloudImage):
            return value

        return parse_image(value)

    def get_prep_value(self, value):
        if value:
            string_value = str(value.upload_to) + ',' + str(value.file_name)

            if value.sizes:
                string_value += ',' + get_thumbnails_string(value.sizes)

            return string_value

class CloudImageCharField(models.Field):
    description = "A image storaded in a cloud service."

    def __init__(self, file_name=None, upload_to=None, sizes=None, *args, **kwargs):
        self.file_name = file_name
        self.upload_to = upload_to
        self.sizes = sizes
        super(CloudImageCharField, self).__init__(*args, **kwargs)