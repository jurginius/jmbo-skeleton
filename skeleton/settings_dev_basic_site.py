from skeleton.settings import *


FOUNDRY['layers'] = ('basic',)
SITE_ID = 2
STATIC_URL = '/static/basic/'

INSTALLED_APPS = INSTALLED_APPS + ('everlytic',)

EVERLYTIC = {
    'URL': 'http://praekelt-host2.pmailer.net/api/1.0',
    'API_KEY': 'DwnGAw4ISfcqLmqnGRYrXOeJw8L3eJBS',
    'LIST_ID': 3780    # ECR Subscriptions Test
}
