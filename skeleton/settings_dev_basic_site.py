from skeleton.settings import *


FOUNDRY['layers'] = ('basic',)
SITE_ID = 2
STATIC_URL = '/static/basic/'

INSTALLED_APPS = INSTALLED_APPS + ('everlytic',)
