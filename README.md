# Open WebUI Tools

This repository contains a collection of Python tools for Open WebUI. These tools provide various functionalities, from network diagnostics to weather forecasts.

## Tools

### `arp.py`

This tool provides a function to perform an ARP scan on a given host to retrieve its MAC address.

**Function:**

*   `arp_scan(host: str)`: Performs an ARP scan on the specified host and returns the MAC address.

### `date-time.py`

This tool provides a simple function to get the current date and time.

**Function:**

*   `get_current_datetime()`: Returns the current date and time as a formatted string.

### `ip-reputation.py`

This tool uses the VirusTotal API to look up the reputation of IP addresses and URLs.

**Functions:**

*   `lookup_ip(ip_address: str)`: Queries VirusTotal for information about the given IP address.
*   `lookup_url(url: str)`: Queries VirusTotal for information about the given URL.

**Dependency:**

*   `requests`

### `nmap.py`

This tool provides a wrapper for the `nmap` command to perform network scans.

**Function:**

*   `nmap_scan(dest: str, options: str = "-sV")`: Performs an Nmap scan on the specified destination with the given options.

**Dependency:**

*   `nmap` must be installed on the system.

### `nslookup.py`

This tool provides a wrapper for the `nslookup` command to perform DNS lookups.

**Function:**

*   `nslookup_request(query: str)`: Performs an `nslookup` for the given query.

### `ping.py`

This tool provides a function to ping a host to check for connectivity.

**Function:**

*   `ping_host(host: str)`: Pings the specified host and returns the output.

### `weather.py`

This tool provides functions to get the current weather and a weekly forecast for a given city using the Open-Meteo API.

**Functions:**

*   `get_current_weather(city: str)`: Returns the current weather for the specified city.
*   `get_future_weather_week(city: str)`: Returns the weather forecast for the next week for the specified city.

**Dependency:**

*   `requests`

### `whois.py`

This tool provides a wrapper for the `whois` command to retrieve WHOIS information for a domain or IP address.

**Function:**

*   `whois_query(query: str)`: Performs a `whois` query for the given domain or IP address.
