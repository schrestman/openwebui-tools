import os
import platform
import subprocess


class Tools:
    def __init__(self):
        self.citation = True
        pass

    def nslookup_request(self, query: str) -> str:
        """
        Performs an nslookup request against a hostname or IP address.

        Args:
            query: The hostname or IP address to look up.

        Returns:
            A string containing the nslookup output, or an error message if the lookup fails.
        """
        try:
            # Construct the nslookup command
            command = ["/usr/bin/nslookup", query]

            # Execute the nslookup command
            process = subprocess.run(
                command, capture_output=True, text=True, check=True
            )

            # Return the output
            return process.stdout

        except subprocess.CalledProcessError as e:
            return f"Error during nslookup request: {e.stderr}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

