#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : dl_from_fortinet.py
# Author             : Podalirius (@podalirius_)
# Date created       : 10 Jan 2022

import os

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    session = requests.Session()
    r = session.get('https://www.fortinet.com/products/next-generation-firewall')

    soup = BeautifulSoup(r.content, "lxml")
    links = []
    for element in soup.find_all("div", attrs={"class":"models--specs--title"}):
        a = element.find("a")
        if a is not None:
            if a['href'].startswith("/content/") and a['href'].lower().endswith('.pdf'):
                links.append("https://www.fortinet.com" + a['href'])
    links = sorted(list(set(links)))

    if os.path.exists("./downloaded/"):
        os.system("rm -rf ./downloaded/")
    os.makedirs("./downloaded/", exist_ok=True)

    for link in links:
        filename = os.path.basename(link)
        filename = filename.upper().replace("FORTIGATE", "FortiGate").replace("FORTIWIFI", "FortiWifi")
        filename = filename.replace('_', '-')
        filename = filename.replace('.PDF', '.pdf')
        if filename.endswith('-SERIES.pdf'):
            filename = filename.replace('-SERIES.pdf', ".pdf")
        if filename.endswith('-SERIES-BUNDLE.pdf'):
            filename = filename.replace('-SERIES-BUNDLE.pdf', ".pdf")
        #
        os.system('cd ./downloaded/; wget -q --show-progress "%s" -O "%s"' % (link, filename))
