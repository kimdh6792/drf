from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# import django
# django.setup()


# '셀러리' 프로그램을 위해 기본 장고 설정파일을 설정합니다.
app = Celery('config',
             broker='amqp://rabbitmq',
             backend='amqp://rabbitmq',
             include=['config.celery_tasks'])

# 여기서 문자열을 사용하는 것은 워커(worker)가 자식 프로세스로 설정 객체를 직렬화(serialize)하지 않아도 된다는 뜻입니다.
# 뒤에 namespace='CELERY'는 모든 셀러리 관련 설정 키는 'CELERY_' 라는 접두어를 가져야 한다고 알려줍니다.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

# app.conf.task_default_queue = 'quick_tasks'
# app.conf.task_default_routing_key = 'quick.#'
# app.conf.task_queues = (
#     Queue('quick_tasks', routing_key='quick.#'),
#     Queue('slow_tasks', routing_key='slow.#'),
# )

# 등록된 장고 앱 설정에서 task를 불러옵니다.
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()
