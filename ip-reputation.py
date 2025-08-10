import requests


def lookup_ip(ip_address: str) -> str:
    """
    Query VirusTotal for threat intelligence related to the given IP address.
    Returns a summary of the results.
    """
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {
        "x-apikey": "YOUR-API-KEY"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        attributes = data.get("data", {}).get("attributes", {})
        last_analysis_stats = attributes.get("last_analysis_stats", {})
        malicious_count = last_analysis_stats.get("malicious", 0)
        categories = attributes.get("categories", [])
        country = attributes.get("country", "N/A")
        as_owner = attributes.get("as_owner", "N/A")

        summary = (
            f"Malicious detections: {malicious_count}, "
            f"Categories: {', '.join(categories)}, "
            f"Country: {country}, "
            f"AS Owner: {as_owner}"
        )
        return summary

    except requests.exceptions.RequestException as e:
        return f"Error querying VirusTotal: {str(e)}"
    except KeyError as e:
        return f"Unexpected response structure: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


def lookup_url(url: str) -> str:
    """
    Query VirusTotal for threat intelligence related to the given URL.
    Returns a summary of the results.
    """
    encoded_url = requests.utils.quote(url)
    url = f"https://www.virustotal.com/api/v3/urls/{encoded_url}"
    headers = {
        "x-apikey": "YOUR-API-KEY"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        attributes = data.get("data", {}).get("attributes", {})
        last_analysis_stats = attributes.get("last_analysis_stats", {})
        malicious_count = last_analysis_stats.get("malicious", 0)
        categories = attributes.get("categories", [])
        url_value = attributes.get("url", "N/A")

        summary = (
            f"Malicious detections: {malicious_count}, "
            f"Categories: {', '.join(categories)}, "
            f"URL: {url_value}"
        )
        return summary

    except requests.exceptions.RequestException as e:
        return f"Error querying VirusTotal: {str(e)}"
    except KeyError as e:
        return f"Unexpected response structure: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


class Tools:
    """
    A class encapsulating the threat intelligence lookup functions.
    """

    def __init__(self):
        self.citation = True  # Placeholder for any future use

    def lookup_ip(self, ip_address: str) -> str:
        return lookup_ip(ip_address)

    def lookup_url(self, url: str) -> str:
        return lookup_url(url)

