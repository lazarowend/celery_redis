
# Programação distribuída com python e celery

Simples exemplo de como criar uma aplicação escalável com celery e REDIS.


## Instalação

Instalação do REDIS
```
sudo apt install redis
redis-cli --version
```

Clone o repositório
```bash
git clone "https://github.com/lazarowend/celery_redis.git"
```
Crie o ambiente virtual
``` bash
python3 -m venv venv
source venv/bin/activate
```
Instale as dependencias
``` bash
pip install -r requirements.txt

```
Inicie o WORKER e o FLOWER
```
celery -A tarefas worker --loglevel=INFO 

celery -A tarefas flower  --address=127.0.0.1 --basic_auth=user:password
```
Inicie os seus testes
```
python3 app.py
```



## Documentação

[Python](https://www.python.org/doc/)\
[Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)\
[Redis](https://redis.io/docs/latest/get-started/)\
[Flower](https://flower.readthedocs.io/en/latest/)

