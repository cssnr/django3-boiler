from celery import shared_task
from celery.utils.log import get_task_logger
from django.core import management

logger = get_task_logger(__name__)


@shared_task()
def clear_sessions():
    return management.call_command('clearsessions')
