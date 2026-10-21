import psutil
import socket


class NetworkMonitor:

    def get_interfaces(self):
        interfaces = []

        addresses = psutil.net_if_addrs()

        for interface_name, address_list in addresses.items():

            interface_info = {
                "interface": interface_name,
                "ipv4": None,
                "mac": None
            }

            for address in address_list:

                if address.family == socket.AF_INET:
                    interface_info["ipv4"] = address.address

                elif address.family == psutil.AF_LINK:
                    interface_info["mac"] = address.address

            interfaces.append(interface_info)

        return interfaces

    def get_network_usage(self):
        stats = psutil.net_io_counters()

        return {
            "bytes_sent": stats.bytes_sent,
            "bytes_received": stats.bytes_recv,
            "packets_sent": stats.packets_sent,
            "packets_received": stats.packets_recv
        }

    def get_connections(self):

        connections = []

        try:
            for connection in psutil.net_connections(kind="inet"):

                connections.append({
                    "fd": connection.fd,
                    "family": str(connection.family),
                    "type": str(connection.type),
                    "local_address": str(connection.laddr),
                    "remote_address": str(connection.raddr),
                    "status": connection.status,
                    "pid": connection.pid
                })

        except psutil.AccessDenied:
            pass

        return connections


if __name__ == "__main__":

    monitor = NetworkMonitor()

    print("=" * 80)
    print("                 SECURESHIELD NETWORK MONITOR")
    print("=" * 80)

    # Network interfaces
    print("\nNETWORK INTERFACES")
    print("-" * 80)

    interfaces = monitor.get_interfaces()

    for interface in interfaces:

        print(f"Interface : {interface['interface']}")
        print(f"IPv4      : {interface['ipv4']}")
        print(f"MAC       : {interface['mac']}")
        print()

    # Network usage
    usage = monitor.get_network_usage()

    print("NETWORK USAGE")
    print("-" * 80)

    print(f"Bytes Sent     : {usage['bytes_sent']}")
    print(f"Bytes Received : {usage['bytes_received']}")
    print(f"Packets Sent   : {usage['packets_sent']}")
    print(f"Packets Received: {usage['packets_received']}")

    # Connections
    connections = monitor.get_connections()

    print("\nACTIVE CONNECTIONS")
    print("-" * 80)

    print(f"Total Connections : {len(connections)}")

    for connection in connections[:20]:

        print(
            f"PID={connection['pid']} | "
            f"Local={connection['local_address']} | "
            f"Remote={connection['remote_address']} | "
            f"Status={connection['status']}"
        )

    print("-" * 80)
    print("\nNetwork monitoring completed.")