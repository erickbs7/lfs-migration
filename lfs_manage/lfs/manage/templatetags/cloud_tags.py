from django import template
from django.template.defaulttags import autoescape
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

# @register.simple_tag
# def cloud_image_thumbnail(image, thumbnail_size):
#     size = thumbnail_size.split(",")
#     url = image.image.get_url(tuple(size))
#     result = ''
#
#     if autoescape:
#         esc = conditional_escape
#     else:
#         esc = lambda x: x
#
#     if url:
#         < img
#         itemprop = "image"
#         src = "{{ product_image.image.url_200x200 }}"
#         title = "{{ product_image.title }}"
#         alt = "{{ product_image.title }}" / >
#
#         result = '<img itemprop="image" src="%s" alt="%s" title="%s" style="float:left"/>' % (esc(url), esc(image.title), esc(image.title))
#     else:
#         result = '<strong>Image not available.</strong>'
#
#     return mark_safe(result)

@register.simple_tag
def cloud_image_thumbnail(image, thumbnail_size):
    size = thumbnail_size.split(",")
    url = image.image.get_url(tuple(size))
    result = ''

    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    if url:
        result = '<img src="%s" alt="%s" title="%s" style="float:left"/>' % (esc(url), esc(image.title), esc(image.title))
    else:
        result = '<strong>Image not available.</strong>'

    return mark_safe(result)

@register.simple_tag(takes_context=True)
def cloud_image(context, thumbnail_size=None):
    category = context['category']
    url = None
    if category.image:
        url = category.image.get_url(thumbnail_size)
    result=''

    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    if url:
        result = '<img src="%s"/>' % (esc(url))
    else:
        # result = '<strong>Image not available.</strong>'
        result = '<br>'

    return mark_safe(result)
