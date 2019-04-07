from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment

from .filters import isList, extractNumber

def environment(**options):

    env = Environment(**options)

    env.tests['isList'] = isList
    env.filters['extractNumber'] = extractNumber

    env.globals.update({
        'static' : staticfiles_storage.url,
        'url' : reverse,
    })

    return env