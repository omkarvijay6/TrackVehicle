from datetime import timedelta

BROKER_URL = "redis://localhost:6379/"
BROKER_TRANSPORT_OPTIONS = {'fanout_prefix': True, 'fanout_patterns': True, 'visibility_timeout': 480}
CELERY_RESULT_BACKEND = BROKER_URL

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'vehicle.tasks.add',
        'schedule': timedelta(seconds=5),
        'args': (16, 16)
    },
}
