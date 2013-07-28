DEBUG = True

PORT = "8888"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
		'simple': {
			'format' : "",
		    'datefmt' : "%d/%b/%Y %H:%M:%S"
		}
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
		'file':{
		    'level': 'DEBUG',
		    'class': 'logging.FileHandler',
	            'filename': 'debug.log',
		}
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': False,
            'level':'DEBUG',
        },
        'werkzeug': {
            'handlers':['console'],
            'propagate': False,
            'level':'WARNING',
        },
       'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'apps': {
            'handlers': ['console','file'],
            'level': 'DEBUG',
        },
    }
}
