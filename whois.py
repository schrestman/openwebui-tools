import os
import platform
import subprocess


class Tools:
    def __init__(self):
        self.citation = True
        pass

    def whois_query(self, query: str) -> str:
        """
        Performs a whois query against a domain or network.

        Args:
            query: The domain or network to look up.

        Returns:
            A string containing the whois output, or an error message if the query fails.
        """
        try:
            # Construct the whois command
            command = ["whois", query]

            # Execute the whois command
            process = subprocess.run(
                command, capture_output=True, text=True, check=True
            )

            # Return the output
            return process.stdout

        except subprocess.CalledProcessError as e:
            return f"Error during whois query: {e.stderr}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

