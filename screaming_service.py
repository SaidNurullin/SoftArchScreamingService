import pika
import time


def callback(ch, method, properties, body):
    message = body.decode().upper()
    channel.basic_publish(exchange='', routing_key='email_queue', body=message)
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    time.sleep(20)
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='uppercase_queue')
    channel.queue_declare(queue='email_queue')
    channel.basic_consume(queue='uppercase_queue', on_message_callback=callback)
    print('Screaming service started. Waiting for messages.')
    channel.start_consuming()
