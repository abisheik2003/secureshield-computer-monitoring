from security.security_logger import SecurityLogger


class AlertManager:

    def __init__(self):

        self.logger = SecurityLogger()

    def create_alert(self, title, severity, message):

        severity = severity.upper()

        alert = {
            "title": title,
            "severity": severity,
            "message": message
        }

        if severity == "HIGH":

            print("\n" + "!" * 60)
            print("              HIGH SECURITY ALERT")
            print("!" * 60)

            print(f"Title    : {title}")
            print(f"Severity : {severity}")
            print(f"Message  : {message}")

            print("!" * 60)

            self.logger.alert(
                f"{title} | {severity} | {message}"
            )

        elif severity == "MEDIUM":

            print("\n" + "-" * 60)
            print("             MEDIUM SECURITY ALERT")
            print("-" * 60)

            print(f"Title    : {title}")
            print(f"Severity : {severity}")
            print(f"Message  : {message}")

            print("-" * 60)

            self.logger.warning(
                f"{title} | {severity} | {message}"
            )

        else:

            print("\nLOW SECURITY EVENT")

            print(f"Title    : {title}")
            print(f"Severity : {severity}")
            print(f"Message  : {message}")

            self.logger.info(
                f"{title} | {severity} | {message}"
            )

        return alert


if __name__ == "__main__":

    alert_manager = AlertManager()

    print("=" * 60)
    print("          SECURESHIELD ALERT MANAGER")
    print("=" * 60)

    alert_manager.create_alert(
        "Test Information",
        "LOW",
        "SecureShield test event."
    )

    alert_manager.create_alert(
        "Test Warning",
        "MEDIUM",
        "A medium severity test event was generated."
    )

    alert_manager.create_alert(
        "Test Security Alert",
        "HIGH",
        "A high severity test event was generated."
    )

    print("\nAlert management test completed.")