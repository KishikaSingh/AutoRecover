import boto3
from botocore.exceptions import ClientError

from AutoRecover.lambda_code.config import SNS_TOPIC_ARN, AWS_REGION
from AutoRecover.lambda_code.logger_config import get_logger

logger = get_logger(__name__)

sns_client = boto3.client(
    "sns",
    region_name=AWS_REGION
)


def send_notification(subject, message):
    """
    Sends a notification to the configured SNS topic.
    """

    try:

        logger.info("Sending SNS notification...")

        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=subject,
            Message=message
        )

        logger.info("SNS notification sent successfully.")

        return response

    except ClientError as error:

        logger.error(f"Failed to send SNS notification: {error}")

        raise