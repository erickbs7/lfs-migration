from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


class LFSImageInput(forms.FileInput):
    """A custom image widget which displays the current image.
    """
    def render(self, name, value, attrs=None):

        output = super(LFSImageInput, self).render(name, None, attrs=attrs)

        # if value and hasattr(value, "url_60x60"):
        #     output += u"""<div><img src="%s" /></div>""" % value.url_60x60
        # elif value and hasattr(value, "url"):
        #     output += u"""<div><img src="%s" /></div>""" % value.url

        # TODO: Refactoring point.
        if value and value.thumbnail_exist((60, 60)):
            print(value.get_url((60, 60)))
            output += u"""<div><img src="%s" /></div>""" % value.get_url((60, 60))
        elif value:
            print(value.get_url())
            output += u"""<div><img src="%s" /></div>""" % value.get_url()

        if value:
            trans = _(u"Delete image")
            output += """<div><input type="checkbox" name="delete_image" id="id_delete_image" /> <label for="delete_image">%s</label></div>""" % unicode(trans)

        return mark_safe(output)
