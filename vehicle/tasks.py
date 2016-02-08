from celery import Celery

app = Celery('vehicle', broker='redis://localhost:6379/')
from vehicle.services import update_test_data

@app.task
def add(x, y):
    print "updated the test data file"
    update_test_data()
