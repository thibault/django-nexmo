INSTALLED_APPS = (
    'djexmo',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
SECRET_KEY = "gloubiboulga secret key"
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

NEXMO_API_KEY = 'API_KEY'
NEXMO_API_SECRET = 'SECRET'
NEXMO_DEFAULT_FROM = '+33123456789'
