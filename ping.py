import os
import platform
import subprocess


def ping_host(host: str) -> str:
    """
    Pings a host and returns the output.

    Args:
        host: The hostname or IP address to ping.

    Returns:
        A string containing the ping output, or an error message if the ping fails.
    """
    try:
        # Determine the operating system
        os_name = platform.system().lower()

        # Construct the ping command based on the operating system
        if os_name == "windows":
            command = ["ping", "-n", "1", host]
        else:  # Assume Linux or macOS
            command = ["ping", "-c", "1", host]

        # Execute the ping command
        process = subprocess.run(command, capture_output=True, text=True, check=True)

        # Return the output
        return process.stdout

    except subprocess.CalledProcessError as e:
        return f"Error pinging {host}: {e.stderr}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


class Tools:
    def init(self):
        self.citation = True
        pass

    def ping_host(self, host: str) -> str:
        """
        Pings a host and returns the output.

        Args:
            host: The hostname or IP address to ping.

        Returns:
            A string containing the ping output, or an error message if the ping fails.
        """
        return ping_host(host)

