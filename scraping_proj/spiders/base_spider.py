import logging

import google.cloud.logging
from scrapy import Spider
from scrapy.http.request import Request
from google.cloud.logging.handlers import CloudLoggingHandler


class BaseSpider(Spider):
    def __init__(self, *args, **kwargs):
        """This class by be inherited by other spiders.

        Any concrete spider inheriting this base spider can send logs
        to Google Logging.
        """
        super().__init__(*args, **kwargs)

    def start_requests(self):
        """Start Scrapy requests.

        For demonstration, the URLs are sent to Google Logging.
        """
        for url in self.start_urls:
            self.logger.info("Spider %s: scraping %s", self.name, url)
            request = Request(url=url, callback=self.parse)
            yield request

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        """Add custom settings for spiders.

        We can only get the settings before a spider is created in a
        crawler.
        """
        spider = cls(*args, **kwargs)
        spider._set_crawler(crawler)
        spider.setup_google_logger()

        return spider

    def setup_google_logger(self):
        """Set up Google Logger for a spider.

        This method can only be called inside the `from_crawler` because
        we need to access the settings. If you call this method
        directly for a spider, an exception will be raised.
        """
        google_logging_client = google.cloud.logging.Client()
        google_logging_handler = CloudLoggingHandler(
            google_logging_client, name=self.name
        )

        log_level = self.settings.get("LOG_LEVEL")
        google_logging_handler.setLevel(log_level)

        logger = logging.getLogger(self.name)
        logger.setLevel(log_level)
        logger.addHandler(google_logging_handler)
