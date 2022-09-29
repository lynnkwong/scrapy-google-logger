import logging
import sys

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
stream_handler.setFormatter(FORMATTER)

logger = logging.getLogger("My Application")
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)

logger.info("This is an info.")
logger.warning("This is a warning.")
logger.error("This is an error.")

# 2022-10-02 23:16:52,264 - My Application - INFO - This is an info.
# 2022-10-02 23:16:52,264 - My Application - WARNING - This is a warning.
# 2022-10-02 23:16:52,264 - My Application - ERROR - This is an error.