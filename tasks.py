from celery import Celery
from random import randint

app = Celery(broker='redis://127.0.0.1:6379/0')


@app.task(bind=True, default_retry_delay=2, max_retries=10, autoretry_for=(ZeroDivisionError, ))
def exibir(self):
    n1 = randint(1, 10)
    if n1 < 5:
        self.retry(countdown = 2*self.request.retries)
        raise ZeroDivisionError('erro kkkkk')
    
    return 'ok'