import os
import platform
import subprocess


def arp_scan(host: str) -> str:
    """
    Performs an ARP scan on a host and returns the MAC address.
    Args:
        host: The IP address of the host to scan.
    Returns:
        A string containing the MAC address, or an error message if the scan fails.
    """
    try:
        os_name = platform.system().lower()
        if os_name == "windows":
            command = ["arp", "-a", host]
        else:  # Assume Linux or macOS
            command = ["arp", "-n", host]

        # Attempt to locate the arp executable
        if os_name == "windows":
            arp_path = "arp"  # Windows typically has arp in the PATH
        else:
            arp_path = "arp"  # Assumes arp is in PATH on Linux/macOS

        process = subprocess.run(
            [arp_path] + command, capture_output=True, text=True, check=True
        )
        output = process.stdout
        # Extract MAC address from output (this might need adjustment based on output format)
        lines = output.splitlines()
        for line in lines:
            if host in line:
                parts = line.split()
                if len(parts) > 2:  # Assuming MAC is the third element
                    return parts[2]
        return "MAC address not found in ARP table."
    except subprocess.CalledProcessError as e:
        return f"Error performing ARP scan: {e.stderr}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


class Tools:
    def init(self):
        self.citation = True
        pass

    def arp_scan(self, host: str) -> str:
        """
        Performs an ARP scan on a host and returns the MAC address.
        Args:
            host: The IP address of the host to scan.
        Returns:
            A string containing the MAC address, or an error message if the scan fails.
        """
        return arp_scan(host)

