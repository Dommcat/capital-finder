from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests  # requests - #TH Code Source Reference watch out for initalized error that happend to roger i.e Requests
import platform


class handler(BaseHTTPRequestHandler):
    """
    An HTTP request handler class that inherits from the BaseHTTPRequestHandler
    class in the http.server module of Python.
    """

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        given_dictionary = dict(query_string_list)
        # Reference country and capital from TH Code
        country = given_dictionary.get("country")
        capital = given_dictionary.get("capital")
        if country:
            country_url = f"https://restcountries.com/v3.1/name/{country}"
            req = requests.get(country_url)
            print("country", req.content)
            data = req.json()
            capital_name = data[0]["capital"][0]
            retrieved_capital = f"The capital of {country.title()} is {capital_name}"

        elif capital:
            capital_url = f"https://restcountries.com/v3.1/capital/{capital}"
            req = requests.get(capital_url)
            print("capital", req.content)
            data = req.json()
            country_name = data[0]["name"]["common"]
            retrieved_capital = f"{capital.title()} is capital of {country_name} "
        else:
            message = "Please input a capital city or country"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        message += " " + platform.python_version()
        self.wfile.write(message.encode())

        return


handle = handler
handle.do_GET()
