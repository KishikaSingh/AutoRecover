import os

INSTANCE_ID = os.getenv("INSTANCE_ID")
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")