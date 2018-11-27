broker_url = 'amqp://XXXX:XXXX@XXXX:XXXX//'
result_backend = 'rpc://'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True
beat_schedule = {
	'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 2.0,
        'args': (16, 16)
    },
}
