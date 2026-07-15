import logging
from AutoRecover.lambda_code.config import LOG_LEVEL


def get_logger(name: str):
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        force=True
    )

    return logging.getLogger(name)