import datetime
from typing import Any


def get_current_datetime() -> str:
    """
    Retrieves the current date and time as a formatted string.
    """
    now = datetime.datetime.now()
    formatted_datetime = now.strftime(
        "%Y-%m-%d %H:%M:%S"
    )  # Customize the format as needed
    return formatted_datetime


class Tools:
    def init(self):
        self.citation = True
        pass

    def get_current_datetime(self) -> str:
        """
        Retrieves the current date and time as a formatted string.

        Returns:
            A string containing the formatted date and time.
        """
        return get_current_datetime()

