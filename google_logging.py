# pip install google-cloud-logging
import logging

import google.cloud.logging

client = google.cloud.logging.Client()

client.setup_logging()
logging.warning("This is a warning from root logger!")

# Use the native logger from logging.
native_logger = logging.getLogger("Native Logger")
native_logger.warning("This is a warning from custom logger.")

# Use the Google logger:
google_logger = client.logger("google_logger")
google_logger.log_text(
    "A warning in text from Google logger.", severity="WARNING"
)
google_logger.log_struct(
    {"error": "An error in JSON from Google logger.", "level": "high"},
    severity="WARNING",
)
