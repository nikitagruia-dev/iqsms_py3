import urllib.request as urllib_request
import urllib.parse as urllib_parse


class Gate:
    """class for using iqsms.ru service via GEs requests"""

    __host = 'gate.iqsms.ru'

    def __init__(self, api_login, api_password):
        self.login = api_login
        self.password = api_password

    def __send_request(self, uri, params=None):
        url = self.__get_url(uri, params)
        request = urllib_request.Request(url)
        pass_man = urllib_request.HTTPPasswordMgrWithDefaultRealm()
        pass_man.add_password(None, url, self.login, self.password)
        auth_handler = urllib_request.HTTPBasicAuthHandler(pass_man)
        try:
            opener = urllib_request.build_opener(auth_handler)
            data = opener.open(request).read()
            return data
        except IOError as e:
            return e.errno

    def __get_url(self, uri, params=None):
        url = "http://%s/%s/" % (self.get_host(), uri)
        param_str = ''
        new_params = {}
        if params is not None:
            for k, v in params.items():
                if v is not None:
                    new_params.update({k: v})
            param_str = urllib_parse.urlencode(new_params)
        return "%s?%s" % (url, param_str)

    def get_host(self):
        """Return current requests host """
        return self.__host

    def set_host(self, host):
        """Changing default requests host """
        self.__host = host

    def send(self, phone, text, sender='iqsms',
             status_queue_name=None, schedule_time=None, wap_url=None):
        """Sending sms """
        params = {'phone': phone,
                  'text': text,
                  'sender': sender,
                  'statusQueueName': status_queue_name,
                  'scheduleTime': schedule_time,
                  'wapurl': wap_url
                  }
        return self.__send_request('send', params)

    def status(self, identifier):
        """Retrieve sms status by it's id """
        params = {'id': identifier}
        return self.__send_request('status', params)

    def status_queue(self, status_queue_name, limit=5):
        """Retrieve latest statuses from queue """
        params = {'statusQueueName': status_queue_name, 'limit': limit}
        return self.__send_request('statusQueue', params)

    def credits(self):
        """Retrieve current credit balance """
        return self.__send_request('credits')

    def senders(self):
        """Retrieve available signs """
        return self.__send_request('senders')


if __name__ == "__main__":
    print(Gate.__doc__)
