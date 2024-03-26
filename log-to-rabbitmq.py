# Via: https://h3xagn.com/streaming-logs-using-rabbitmq/#file-rabbitmq-producer-py
# Via: https://gist.github.com/h3xagn/8e0f26f8b09937eacc5fe33937f9481a#file-rabbitmq-producer-py

# import libraries
import logging
from python_logging_rabbitmq import RabbitMQHandler

logname = "log_example_for_task.txt"

# configure the logging tool
logger = logging.getLogger("siuntejas")
logger.setLevel(logging.INFO)

# configure RabbitMQ logger
rabbit = RabbitMQHandler(
    host="localhost",
    port=5672,
    exchange="amq.topic",
)

# add RMQ logger to the logging tool
logger.addHandler(rabbit)

# open the log file and read the content
logfile = open(logname, "r")
lines = logfile.readlines()

for line in lines:
    logger.info(line)
