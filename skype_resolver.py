from __future__ import print_function
import Skype4Py
import sys
import re
import threading
import requests


class main:
    def __init__(self):
        self.geoLocators = ['http://ip-api.com/json/%s']
        self.ip2skype = 'http://resolveme.org/ip2skype.php?do=resolve'
        self.resolvers = ['http://api.resolver.in/?key=1664bc6b1975904165e5a1fe73dd84e9b8d24f99&username=%s',]
        self.target = sys.argv[1]
        for resolver in self.resolvers:
            for ip in requests.get(resolver%self.target).text.encode('utf-8').split('||'):
                ip = ip.strip().rstrip().split("|")[0]
                print("[+] %s using <<%s>> and found it on %s"%(ip, self.geoLocate(ip), self.doIp2Skype(ip)['error']))

    def geoLocate(self, ip):
        for geo in self.geoLocators:
            return requests.get(geo%ip).json()['isp']

    def doIp2Skype(self, ip):
        return {'error': 'not implemented'}

if __name__ == "__main__":
    main()