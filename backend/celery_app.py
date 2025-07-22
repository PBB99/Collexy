from celery import Celery

def make_celery(app):
    celery=Celery