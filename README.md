# celery-example

```
virtualenv venv
source venv/bin/activate
pip install Celery
```

```
celery -A tasks worker --loglevel=info
```

以下在另一个终端
```
python main.py
```

```
celery -A tasks beat
```