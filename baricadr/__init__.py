from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests

from baricadr.exceptions import BaricadrConnectionError
from baricadr.file import FileClient
from baricadr.task import TaskClient

from future import standard_library

standard_library.install_aliases()

class BaricadrInstance(object):

    def __init__(self, host="localhost", port="9100", **kwargs):
        self.host = host
        self.port = str(port)

        self._test_access()

        # Initialize Clients
        args = (self.host, self.port)
        self.file = FileClient(*args)
        self.task = TaskClient(*args)

    def __str__(self):
        return '<BarricadrInstance at {}:{}>'.format(self.host, self.port)

    def _test_access(self):
        try:
            r = requests.get("http://{}:{}".format(self.host,self.port))
            if not r.status_code == 200:
                raise requests.exceptions.RequestException
        except requests.exceptions.RequestException:
            raise BaricadrConnectionError("Cannot connect to {}:{}. Please check the connection.".format(self.host,self.port))