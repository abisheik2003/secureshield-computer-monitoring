import logging
import os


class SecurityLogger:

    def __init__(self, log_file="security.log"):

        self.log_file = log_file

        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        self.logger = logging.getLogger("SecureShield")

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def alert(self, message):
        self.logger.critical(message)


if __name__ == "__main__":

    logger = SecurityLogger()

    logger.info("SecureShield security logger started.")

    logger.info("System monitoring completed.")

    logger.warning("Test warning event generated.")

    logger.error("Test error event generated.")

    logger.alert("Test security alert generated.")

    print("=" * 60)
    print("       SECURESHIELD SECURITY LOGGER")
    print("=" * 60)

    print("\nSecurity logging test completed.")

    print(f"Log file: {os.path.abspath(logger.log_file)}")