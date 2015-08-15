import os
from settings import *

SITENAME = 'GEONODE'
SITEURL = 'http://192.168.1.206/'
REGISTRATION_OPEN = False
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'geonodeemail@gmail.com'
EMAIL_HOST_PASSWORD = 'geonodeemailpassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'geonode',
         'USER': 'geonode',
         'PASSWORD': 'password', # adjust as set above
     },
    # vector datastore for uploads
    'datastore' : {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        #'ENGINE': '', # Empty ENGINE name disables 
        'NAME': 'geonode-imports',
        'USER' : 'geonode',
        'PASSWORD' : 'password', # adjust as set above
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION' : 'http://192.168.1.206/geoserver/',
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIG_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : False,
        'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': 'datastore', #'datastore',
    }
}

# CSW settings
CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        # 'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
        # 'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        'USER': 'admin',
        'PASSWORD': 'admin',
    }
}

# Documents application
ALLOWED_DOCUMENT_TYPES = [
    'csv', 'doc', 'docx', 'gif', 'jpg', 'jpeg', 'ods', 'odt', 'odp', 'pdf', 'png', 'ppt',
    'pptx', 'rar', 'tif', 'tiff', 'txt', 'xls', 'xlsx', 'xml', 'zip', 'gz'
]
MAX_DOCUMENT_SIZE = 2  # MB
DOCUMENT_TYPE_MAP = {
    'csv': 'text',
    'txt': 'text',
    'log': 'text',
    'doc': 'text',
    'docx': 'text',
    'ods': 'text',
    'odt': 'text',
    'xls': 'text',
    'xlsx': 'text',
    'xml': 'text',

    'gif': 'image',
    'jpg': 'image',
    'jpeg': 'image',
    'png': 'image',
    'tif': 'image',
    'tiff': 'image',

    'odp': 'presentation',
    'ppt': 'presentation',
    'pptx': 'presentation',
    'pdf': 'presentation',

    'rar': 'archive',
    'gz': 'archive',
    'zip': 'archive',
}

ALLOWED_HOSTS = ['192.168.1.206']

# Default preview library
#LAYER_PREVIEW_LIBRARY = 'geoext'
