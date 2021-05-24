#!/usr/bin/env python3
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import re


def verify_url(url):
    """Check if the specified URL is a Google Play Store URL

    :param url: Google Play Store URL
    """
    verified = False

    url_parsed = urlparse(url)
    netloc = url_parsed.netloc
    path = url_parsed.path

    if netloc == "play.google.com" and (path == "/store/apps/developer" or path == "/store/apps/dev"
                                        or path == "/store/apps/collection/cluster"):
        verified = True

    return verified


def app_horizontal_enumeration(company_url):
    """Get all application developed by the same company

    :param company_url: URL of the company
    """
    print(">> Scrapping associated applications")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    request1 = requests.get(company_url, headers=headers)
    request2 = requests.get(company_url)
    app_list = []

    if request1.status_code == 200:
        # Processing the query with an User-Agent
        soup_parse = BeautifulSoup(request1.text, 'html.parser')

        for a in soup_parse.find_all('a', href=re.compile("^/store/apps/details\?id=")):
            app_list.append(a['href'])

        # Processing the query without an User-Agent
        soup_parse = BeautifulSoup(request2.text, 'html.parser')

        for a in soup_parse.find_all('a', href=re.compile("^/store/apps/details\?id=")):
            app_list.append(a['href'])

        # Get uniq applications
        unique_apps = set(app_list)

        # Display application
        for element in unique_apps:
            print("https://play.google.com%s" % element)

        return unique_apps


def download_app(app_list):
    """Download all application developed by the same company

    :param app_list: List of unique application
    """
    print("\n>> Download applications")
    print("Coming soon")
