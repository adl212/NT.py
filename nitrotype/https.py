import ssl, requests
try:
    import copyreg
except ImportError:
    import copy_reg as copyreg
from requests.adapters import HTTPAdapter
class CipherSuiteAdapter(HTTPAdapter):

    __attrs__ = [
        'ssl_context',
        'max_retries',
        'config',
        '_pool_connections',
        '_pool_maxsize',
        '_pool_block',
        'source_address'
    ]

    def __init__(self, *args, **kwargs):
        self.ssl_context = kwargs.pop('ssl_context', None)
        self.cipherSuite = kwargs.pop('cipherSuite', None)
        self.source_address = kwargs.pop('source_address', None)

        if self.source_address:
            if isinstance(self.source_address, str):
                self.source_address = (self.source_address, 0)

            if not isinstance(self.source_address, tuple):
                raise TypeError(
                    "source_address must be IP address string or (ip, port) tuple"
                )

        if not self.ssl_context:
            self.ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            self.ssl_context.set_ciphers(self.cipherSuite)
            self.ssl_context.set_ecdh_curve('prime256v1')
            self.ssl_context.options |= (ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)

        super(CipherSuiteAdapter, self).__init__(**kwargs)

    # ------------------------------------------------------------------------------- #

    def init_poolmanager(self, *args, **kwargs):
        kwargs['ssl_context'] = self.ssl_context
        kwargs['source_address'] = self.source_address
        return super(CipherSuiteAdapter, self).init_poolmanager(*args, **kwargs)

    # ------------------------------------------------------------------------------- #

    def proxy_manager_for(self, *args, **kwargs):
        kwargs['ssl_context'] = self.ssl_context
        kwargs['source_address'] = self.source_address
        return super(CipherSuiteAdapter, self).proxy_manager_for(*args, **kwargs)
import json
import os
import random
import re
import sys

from collections import OrderedDict

# ------------------------------------------------------------------------------- #


class User_Agent():

    # ------------------------------------------------------------------------------- #

    def __init__(self, *args, **kwargs):
        self.headers = None
        self.cipherSuite = []
        self.loadUserAgent(*args, **kwargs)

    # ------------------------------------------------------------------------------- #

    def filterAgents(self, user_agents):
        filtered = {}

        if self.mobile:
            if self.platform in user_agents['mobile'] and user_agents['mobile'][self.platform]:
                filtered.update(user_agents['mobile'][self.platform])

        if self.desktop:
            if self.platform in user_agents['desktop'] and user_agents['desktop'][self.platform]:
                filtered.update(user_agents['desktop'][self.platform])

        return filtered

    # ------------------------------------------------------------------------------- #

    def tryMatchCustom(self, user_agents):
        for device_type in user_agents['user_agents']:
            for platform in user_agents['user_agents'][device_type]:
                for browser in user_agents['user_agents'][device_type][platform]:
                    if re.search(re.escape(self.custom), ' '.join(user_agents['user_agents'][device_type][platform][browser])):
                        self.headers = user_agents['headers'][browser]
                        self.headers['User-Agent'] = self.custom
                        self.cipherSuite = user_agents['cipherSuite'][browser]
                        return True
        return False

    # ------------------------------------------------------------------------------- #

    def loadUserAgent(self, *args, **kwargs):
        self.browser = kwargs.pop('browser', None)

        self.platforms = ['linux', 'windows', 'darwin', 'android', 'ios']
        self.browsers = ['chrome', 'firefox']

        if isinstance(self.browser, dict):
            self.custom = self.browser.get('custom', None)
            self.platform = self.browser.get('platform', None)
            self.desktop = self.browser.get('desktop', True)
            self.mobile = self.browser.get('mobile', True)
            self.browser = self.browser.get('browser', None)
        else:
            self.custom = kwargs.pop('custom', None)
            self.platform = kwargs.pop('platform', None)
            self.desktop = kwargs.pop('desktop', True)
            self.mobile = kwargs.pop('mobile', True)

        if not self.desktop and not self.mobile:
            sys.tracebacklimit = 0
            raise RuntimeError("Sorry you can't have mobile and desktop disabled at the same time.")

        with open(os.path.join(os.path.dirname(__file__), 'browsers.json'), 'r') as fp:
            user_agents = json.load(
                fp,
                object_pairs_hook=OrderedDict
            )

        if self.custom:
            if not self.tryMatchCustom(user_agents):
                self.cipherSuite = [
                    ssl._DEFAULT_CIPHERS,
                    '!AES128-SHA',
                    '!ECDHE-RSA-AES256-SHA',
                ]
                self.headers = OrderedDict([
                    ('User-Agent', self.custom),
                    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'),
                    ('Accept-Language', 'en-US,en;q=0.9'),
                    ('Accept-Encoding', 'gzip, deflate, br')
                ])
        else:
            if self.browser and self.browser not in self.browsers:
                sys.tracebacklimit = 0
                raise RuntimeError(f'Sorry "{self.browser}" browser is not valid, valid browsers are [{", ".join(self.browsers)}].')

            if not self.platform:
                self.platform = random.SystemRandom().choice(self.platforms)

            if self.platform not in self.platforms:
                sys.tracebacklimit = 0
                raise RuntimeError(f'Sorry the platform "{self.platform}" is not valid, valid platforms are [{", ".join(self.platforms)}]')

            filteredAgents = self.filterAgents(user_agents['user_agents'])

            if not self.browser:
                # has to be at least one in there...
                while not filteredAgents.get(self.browser):
                    self.browser = random.SystemRandom().choice(list(filteredAgents.keys()))

            if not filteredAgents[self.browser]:
                sys.tracebacklimit = 0
                raise RuntimeError(f'Sorry "{self.browser}" browser was not found with a platform of "{self.platform}".')

            self.cipherSuite = user_agents['cipherSuite'][self.browser]
            self.headers = user_agents['headers'][self.browser]

            self.headers['User-Agent'] = random.SystemRandom().choice(filteredAgents[self.browser])

        if not kwargs.get('allow_brotli', False) and 'br' in self.headers['Accept-Encoding']:
            self.headers['Accept-Encoding'] = ','.join([
                encoding for encoding in self.headers['Accept-Encoding'].split(',') if encoding.strip() != 'br'
            ]).strip()

class idk(requests.Session):
    def __init__(self, *args, **kwargs):
        self.allow_brotli = False
        self.cipherSuite = None
        self.ssl_context = None
        self.source_address = None
        self.user_agent = User_Agent(
            allow_brotli=self.allow_brotli,
            browser=kwargs.pop('browser', None)
        )

        self._solveDepthCnt = 0
        self.solveDepth = kwargs.pop('solveDepth', 3)

        super(idk, self).__init__(*args, **kwargs)
        # pylint: disable=E0203
        if 'requests' in self.headers['User-Agent']:
            # ------------------------------------------------------------------------------- #
            # Set a random User-Agent if no custom User-Agent has been set
            # ------------------------------------------------------------------------------- #
            self.headers = self.user_agent.headers
            if not self.cipherSuite:
                self.cipherSuite = self.user_agent.cipherSuite

        if isinstance(self.cipherSuite, list):
            self.cipherSuite = ':'.join(self.cipherSuite)

        self.mount(
            'https://',
            CipherSuiteAdapter(
                cipherSuite=self.cipherSuite,
                ssl_context=self.ssl_context,
                source_address=self.source_address
            )
        )

        # purely to allow us to pickle dump
        copyreg.pickle(ssl.SSLContext, lambda obj: (obj.__class__, (obj.protocol,)))