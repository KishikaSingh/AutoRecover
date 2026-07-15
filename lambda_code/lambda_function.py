import json

from AutoRecover.lambda_code.logger_config import get_logger
from AutoRecover.lambda_code.config import INSTANCE_ID
from AutoRecover.lambda_code.ec2_service import reboot_instance
from AutoRecover.lambda_code.sns_service import send_notification

logger = get_logger(__name__)


def lambda_handler(event, context):

    logger.info("Lambda function started.")
    logger.info(json.dumps(event, indent=4))

    try:

        alarm_name = (
    event.get("detail", {}).get("alarmName", "Unknown Alarm")
)

        reboot_instance()

        send_notification(
            subject="EC2 Auto Recovery Successful",
            message=f"""
EC2 Auto Recovery Triggered

Alarm Name: {alarm_name}

Instance ID: {INSTANCE_ID}

Action Taken:
Reboot initiated successfully.
"""
        )

        return {
            "statusCode": 200,
            "body": json.dumps("Recovery completed successfully.")
        }

    except Exception as error:

        logger.error(str(error))

        send_notification(
            subject="EC2 Auto Recovery Failed",
            message=f"""
EC2 Auto Recovery Failed

Instance ID: {INSTANCE_ID}

Reason:
{error}
"""
        )

        raise