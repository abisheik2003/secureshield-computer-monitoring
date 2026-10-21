import os


class SuspiciousDetector:

    def __init__(
        self,
        cpu_threshold=80,
        memory_threshold=20
    ):
        self.cpu_threshold = cpu_threshold
        self.memory_threshold = memory_threshold

    def check_process(self, process):
        reasons = []
        score = 0

        cpu = process.get("cpu_percent", 0)
        memory = process.get("memory_percent", 0)
        path = process.get("path", "Unknown")

        # Rule 1: High CPU usage
        if cpu >= self.cpu_threshold:
            reasons.append(
                f"High CPU usage: {cpu:.1f}%"
            )
            score += 40

        # Rule 2: High memory usage
        if memory >= self.memory_threshold:
            reasons.append(
                f"High memory usage: {memory:.1f}%"
            )
            score += 30

        # Rule 3: Executable running from unusual writable locations
        if path != "Unknown":
            path_lower = path.lower()

            suspicious_locations = [
                "\\temp\\",
                "\\appdata\\local\\temp\\",
                "\\downloads\\"
            ]

            for location in suspicious_locations:
                if location in path_lower:
                    reasons.append(
                        f"Executable located in unusual path: {path}"
                    )
                    score += 30
                    break

        # Risk classification
        if score >= 70:
            risk = "HIGH"
        elif score >= 40:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        return {
            "pid": process.get("pid"),
            "name": process.get("name", "Unknown"),
            "score": score,
            "risk": risk,
            "reasons": reasons
        }


if __name__ == "__main__":
    detector = SuspiciousDetector()

    test_process = {
        "pid": 1234,
        "name": "example.exe",
        "cpu_percent": 85.0,
        "memory_percent": 5.0,
        "path": r"C:\Users\Test\AppData\Local\Temp\example.exe"
    }

    result = detector.check_process(test_process)

    print("=" * 60)
    print("       SECURESHIELD SUSPICIOUS ACTIVITY TEST")
    print("=" * 60)

    print(f"\nPID       : {result['pid']}")
    print(f"Process   : {result['name']}")
    print(f"Risk Score: {result['score']}")
    print(f"Risk Level: {result['risk']}")

    print("\nReasons:")

    if result["reasons"]:
        for reason in result["reasons"]:
            print(f"- {reason}")
    else:
        print("- No suspicious indicators detected")

    print("\nDetection test completed.")