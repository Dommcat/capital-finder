from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform # or shouldRequests


class handler(BaseHTTPRequestHandler):
        """
        An HTTP request handler class that inherits from the BaseHTTPRequestHandler
        class in the http.server module of Python.

        This class handles incoming HTTP requests and sends back the appropriate
        response to the client. It can handle various HTTP methods such as GET,
        POST, PUT, and DELETE, and can serve static files, dynamic content, or
        redirect requests to other URLs.

        The methods in this class are automatically called by the server when a
        request is received, and can be overridden to customize the behavior of
        the handler. For example, the do_GET method can be overridden to serve
        custom content instead of a default response.

        Attributes:
            server_version (str): The name and version of the server software.
            sys_version (str): The name and version of the Python interpreter.
            protocol_version (str): The HTTP protocol version used by the server.
            """

        def do_GET(self):
          s = self.path
          url_components = parse.urlsplit(s)
          query_string_list = parse.parse_qsl(url_components.query)
          given_dictionary = dict(query_string_list)
          #Add country and capital 
          name = given_dictionary.get('name')

          if name:
              message = f"Hello {name}.  How are you?"

              # if country:
#             country_url = f'https://restcountries.com/v3.1/name/{country}'
#             req = requests.get(country_url)
#             data = req.json()
#             capital_name = data[0]['capital'][0]
#             retrieved_capital = f'The capital of {country.title()} is {capital_name}'
          
          
          else:
              message = "Please input a capital city or country"
        
        
        
        
        
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          message += " " + platform.python_version()
          self.wfile.write(message.encode())
          return




#TH Code - watch out for initalized error that happend to roger 

# from http.server import BaseHTTPRequestHandler
# from urllib import parse
# import requests


# class handler(BaseHTTPRequestHandler):
#     """
#     Class holds function to GET capital of country or country to which capital belongs.
#     """
#     
# 
# def do_GET(self):
#         s = self.path
#         url_components = parse.urlsplit(s)
#         query_string_list = parse.parse_qsl(url_components.query)
#         given_dictionary = dict(query_string_list)
#         country = given_dictionary.get('country')
#         capital = given_dictionary.get('capital')
#         
# 
# 
# 
# if country:
#             country_url = f'https://restcountries.com/v3.1/name/{country}'
#             req = requests.get(country_url)
#             data = req.json()
#             capital_name = data[0]['capital'][0]
#             retrieved_capital = f'The capital of {country.title()} is {capital_name}'

#         elif capital:
#             capital_url = f'https://restcountries.com/v3.1/capital/{capital}'
#             req = requests.get(capital_url)
#             data = req.json()
#             country_name = data[0]['name']['common']
#             retrieved_capital = f'{capital.title()} is capital of {country_name} '
#         else:
#             retrieved_capital = "Please give me a capital or country"





#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         self.wfile.write(retrieved_capital.encode())
#         return