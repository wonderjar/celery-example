# celery-example

```
virtualenv venv
source venv/bin/activate
pip install Celery
```

```
celery -A tasks worker --loglevel=info
```

```
python main.py
```