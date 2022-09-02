from celery import Celery

app = Celery('hello', broker='sqla+sqlite:///celerydb.sqlite',backend="db+sqlite:///celeryresults.sqlite")
# app = Celery('hello',broker='amqp://',backend='amqp://')
# pip install celery redis sqlalchemy
# celery -A tasks worker --loglevel=INFO --concurrency=2



@app.task
def hello():
    return 'hello world'
