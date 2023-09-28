from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import logging
from service_3.celery import app

logger = logging.getLogger()
channel_layer = get_channel_layer()


@app.task(name='my_sender.task.send_message', queue='data_queue')
def send_message(sms, sender_id):
    text = sender_id + ': ' + sms['text']
    logger.info(text)
    room_name = sms['receiver']
    room_group_name = "chat_%s" % room_name
    async_to_sync(channel_layer.group_send)(
        room_group_name, {'type': 'SMS', 'text': text}
    )

