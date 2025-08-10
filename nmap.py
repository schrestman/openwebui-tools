import os
import platform
import subprocess


class Tools:
    def __init__(self):
        self.citation = True
        pass

    def nmap_scan(self, dest: str, options: str = "-sV") -> str:
        """
        Performs an Nmap scan against a host or network.

        Args:
            dest: The hostname,IP address, or network to scan.
            options: Optional Nmap scan options (e.g., "-sS", "-O", etc.).  Defaults to "-sn" (ping scan).

        Returns:
            A string containing the Nmap scan output, or an error message if the scan fails.
        """
        try:
            # Check if Nmap is installed.  This is crucial!
            try:
                subprocess.run(["nmap", "-version"], capture_output=True, check=True)
            except FileNotFoundError:
                return "Error: Nmap is not installed. Please install it before running this scan."

            # Construct the Nmap command
            command = ["nmap", dest, options]

            # Execute the Nmap command
            process = subprocess.run(
                command, capture_output=True, text=True, check=True
            )

            # Return the output
            return process.stdout

        except subprocess.CalledProcessError as e:
            return f"Error during Nmap scan: {e.stderr}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

