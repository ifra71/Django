from celery import shared_task


@shared_task
def test_celery():
    print("CELERY IS WORKING")


@shared_task
def scheduled_task():
    print("task was run by celery beat ")