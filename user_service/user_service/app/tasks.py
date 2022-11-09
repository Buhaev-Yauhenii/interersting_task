from .celery import app
from celery.utils.log import get_task_logger
from django.core.management import call_command
from .email import preset_email


@app.task
def send_email():
    preset_email()
