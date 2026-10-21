import psutil


class ProcessMonitor:

    def get_processes(self):
        processes = []

        for process in psutil.process_iter(
            [
                "pid",
                "name",
                "username",
                "status",
                "exe"
            ]
        ):
            try:
                cpu_usage = process.cpu_percent(interval=0.1)
                memory_usage = process.memory_percent()

                info = process.info

                processes.append({
                    "pid": info["pid"],
                    "name": info["name"] or "Unknown",
                    "username": info["username"] or "Unknown",
                    "status": info["status"],
                    "path": info["exe"] or "Unknown",
                    "cpu_percent": cpu_usage,
                    "memory_percent": memory_usage
                })

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):
                continue

        return processes


if __name__ == "__main__":

    monitor = ProcessMonitor()
    processes = monitor.get_processes()

    print("=" * 100)
    print("                 SECURESHIELD PROCESS MONITOR")
    print("=" * 100)

    print(f"\nTotal Processes : {len(processes)}\n")

    print("-" * 100)

    print(
        f"{'PID':<8}"
        f"{'PROCESS':<25}"
        f"{'CPU %':<10}"
        f"{'MEM %':<10}"
        f"{'STATUS':<12}"
        f"USERNAME"
    )

    print("-" * 100)

    for process in processes[:30]:

        print(
            f"{process['pid']:<8}"
            f"{process['name'][:23]:<25}"
            f"{process['cpu_percent']:<10.1f}"
            f"{process['memory_percent']:<10.1f}"
            f"{process['status']:<12}"
            f"{process['username'][:20]}"
        )

    print("-" * 100)

    print("\nProcess resource monitoring completed.")