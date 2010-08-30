# Django settings for datahq project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/hqwebapp/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fixme'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'corehq.util.threadlocals.ThreadLocals',
    'auditor.middleware.AuditMiddleware',
    'domain.middleware.DomainMiddleware',
    'django_digest.middleware.HttpDigestMiddleware',
    
)

ROOT_URLCONF = 'urls'


TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "corehq.util.context_processors.base_template" # sticks the base template inside all responses
]


DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    
)

HQ_APPS = (
    'reversion',
    'django_extensions', 
    'django_rest_interface',
    'corehq.lib.django_digest',
    'corehq.lib.django_granular_permissions',
    'corehq.lib.django_tables',
    'corehq.lib.django_user_registration',
    'corehq.apps.domain',
    'corehq.apps.receiver',
    'corehq.apps.xforms',
    'corehq.apps.hqwebapp',
    'corehq.apps.program',
    'corehq.apps.phone',
    'corehq.apps.logtracker',
    'corehq.apps.auditor',
    
    'care_apps.provider',
    'care_apps.keymaster',
    #'care_apps.pactdata',  #hacky note (dmyung): if you get a too long field error on syncdb, comment this out and syncdb, then comment it back in when you want to run
    'care_apps.pactapp',
    'care_apps.pactpatient',
	'care_apps.dots',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = DEFAULT_APPS + HQ_APPS

# after login, django redirects to this URL
# rather than the default 'accounts/profile'
LOGIN_REDIRECT_URL='/'

#Relative paths to the settings.py
####### Receiver Settings #######
RECEIVER_SUBMISSION_PATH="data/submissions"
RECEIVER_ATTACHMENT_PATH="data/attachments"
RECEIVER_EXPORT_PATH="data"

####### XFormManager Settings #######
XFORMS_SCHEMA_PATH="data/schemas"
XFORMS_EXPORT_PATH="data/exports"
XFORMS_FORM_TRANSLATE_JAR="lib/form_translate.jar"

#####Encryption Keys######
KEYSTORE_PATH='data/keystore'


####### Domain settings  #######

DOMAIN_MAX_REGISTRATION_REQUESTS_PER_DAY=99
DOMAIN_SELECT_URL="/domain/select/"
LOGIN_URL="/accounts/login/"
# For the registration app
# One week to confirm a registered user account
ACCOUNT_ACTIVATION_DAYS=7 
# If a user tries to access domain admin pages but isn't a domain 
# administrator, here's where he/she is redirected
DOMAIN_NOT_ADMIN_REDIRECT_PAGE_NAME="homepage"


####### Shared/Global/UI Settings ######

# restyle some templates
BASE_TEMPLATE="hq-layout.html"
LOGIN_TEMPLATE="login_and_password/login.html"
LOGGEDOUT_TEMPLATE="loggedout.html"

#logtracker settings variables
LOGTRACKER_ALERT_EMAILS = []
LOGTRACKER_LOG_THRESHOLD = 30
LOGTRACKER_ALERT_THRESHOLD = 40

# email settings: these ones are the custom hq ones
EMAIL_LOGIN="notifications@dimagi.com"
EMAIL_PASSWORD="alpha321"
EMAIL_SMTP_HOST="smtp.gmail.com"
EMAIL_SMTP_PORT=587

# these are the official django settings
# which really we should be using over the
# above
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "notifications@dimagi.com"
EMAIL_HOST_PASSWORD = "alpha321"
EMAIL_USE_TLS = True

AUDIT_VIEWS = [
               'xforms.views.dashboard',
               'xforms.views.remove_xform',
               'xforms.views.new_form_data_group',
               'xforms.views.submit_data',
               'xforms.views.single_xform',
               'xforms.views.get_xform',
               'xforms.views.export_xml',
               'xforms.views.plain_data',
               'xforms.views.data',
               'xforms.views.export_csv',
               'xforms.views.readable_xform',
               'xforms.views.get_csv_from_form',
               'xforms.views.data',               
               'receiver.views.single_attachment',
               'receiver.views.single_submission',
               'receiver.views.domain_submit',
               'receiver.views.domain_resubmit',
               'receiver.views.orphaned_data',
               'receiver.views.delete_submission',
               'receiver.views.show_submits',
               'receiver.views.show_dupes',               
               ]

AUDIT_MODEL_SAVE = [
                    'django.contrib.auth.models.User', 
                    'xforms.models.Metadata',
                    'xforms.models.FormDefModel',
                    'receiver.models.Submission',
                    'pactpatient.models.IdentifierType',
                    'pactpatient.models.Address',
                    'pactpatient.models.PatientIdentifier',
                    'pactpatient.models.Patient',
                    'provider.models.Provider',
                    'keymaster.models.DeviceKey',                    
                    'domain.models.Domain',
                    'domain.models.Membership',               
                    ]


TABS = [
    ('corehq.apps.hqwebapp.views.dashboard', 'Dashboard'),
    ('corehq.apps.xforms.views.dashboard', 'XForms'),
    ('corehq.apps.receiver.views.show_submits', 'Submissions'),
    ('pactapp.views.progress_notes', 'Progress Notes'),
    # ('program.views.list_programs', 'Programs')
	('dots.views.index', 'DOTS'),
]

DIGEST_ENFORCE_NONCE_COUNT = False

# import local settings if we find them
try:
    from localsettings import *
except ImportError:
    pass
