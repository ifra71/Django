from celery import shared_task

@shared_task
def test_celery():
    print("CELERY IS WORKING")