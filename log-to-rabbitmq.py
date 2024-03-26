# Via: https://h3xagn.com/streaming-logs-using-rabbitmq/#file-rabbitmq-producer-py
# Via: https://gist.github.com/h3xagn/8e0f26f8b09937eacc5fe33937f9481a#file-rabbitmq-producer-py

# import libraries
import time
import logging
from python_logging_rabbitmq import RabbitMQHandler

logger = logging.getLogger("siuntejas")
logger.setLevel(logging.DEBUG)

# configure RabbitMQ logger
rabbit = RabbitMQHandler(
    host="localhost",
    port=5672,
    exchange="amq.topic",
)
logger.addHandler(rabbit)

logfile = open("log_example_for_task.txt", "r")
lines = logfile.readlines()
count = 0

for line in lines:
    count += 1
    print("Line {}: {}".format(count, line.strip()))

logger.info("Sending a sample message")
