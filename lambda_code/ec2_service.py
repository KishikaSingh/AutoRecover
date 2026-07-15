import boto3
from botocore.exceptions import ClientError

from AutoRecover.lambda_code.config import INSTANCE_ID, AWS_REGION
from AutoRecover.lambda_code.logger_config import get_logger

logger = get_logger(__name__)

ec2_client = boto3.client(
    "ec2",
    region_name=AWS_REGION
)


def reboot_instance():
    """
    Reboots the configured EC2 instance.
    """

    try:

        logger.info(f"Initiating reboot for EC2 Instance: {INSTANCE_ID}")

        response = ec2_client.reboot_instances(
            InstanceIds=[INSTANCE_ID]
        )

        logger.info("Reboot request sent successfully.")

        return response

    except ClientError as error:

        logger.error(f"Failed to reboot instance: {error}")

        raise