import threading

import six
from dcos import util
from six import iteritems

from six.moves import urllib
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class ProxyThread(threading.Thread):
    def __init__(self):
        self.proxy = HTTPServer(('localhost', 0), Proxy)
        threading.Thread.__init__(self)

    def run(self):
        return self.proxy.serve_forever()

    def port(self):
        return self.proxy.socket.getsockname()[1]


class Proxy(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self._process_request()

    def do_GET(self):
        self._process_request()

    def do_POST(self):
        self._process_request()

    def do_PUT(self):
        self._process_request()

    def do_PATCH(self):
        self._process_request()

    def do_DELETE(self):
        self._process_request()

    def _add_headers(self, req, toml_config):
        # add headers from client request
        for k, v in iteritems(self.headers):
            req.add_header(k, v)

        # add auth header
        token = toml_config.get("core.dcos_acs_token")
        req.add_header('Authorization', "token={}".format(token))

    def _process_request(self):
        toml_config = util.get_config()

        # urllib.request only supports HTTP 1.0 :(
        # https://docs.python.org/3/library/urllib.request.html
        six.moves.http_client.HTTPConnection._http_vsn = 10
        six.moves.http_client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

        dcos_url = toml_config.get("core.dcos_url")
        url = urllib.parse.urljoin(dcos_url, self.path)

        if self.headers.get('Content-Length') is not None:
            body = self.rfile.read(
                int(self.headers.get('Content-Length', 0)))
            req = urllib.request.Request(url, body)
        else:
            req = urllib.request.Request(url)

        try:
            self._add_headers(req, toml_config)
            resp = urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            resp = e
        self.send_response(resp.getcode())

        for k, v in iteritems(resp.headers):
            self.send_header(k, v)
        self.end_headers()
        resp_body = resp.read()
        self.wfile.write(resp_body)
