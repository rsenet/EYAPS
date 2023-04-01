#!/usr/bin/env python3

from lib.parser import *
import argparse
import sys

__author__  = 'Regis SENET'
__email__   = 'regis.senet@orhus.fr'
__git__     = 'https://github.com/rsenet/EYAPS'
__version__ = '0.1'
__license__ = 'GPLv3'
__pyver__   = '%d.%d.%d' % sys.version_info[0:3]
short_desc  = "Android Application horizontal enumeration"

arg_parser = argparse.ArgumentParser(description=short_desc)
arg_parser.add_argument('--url', help="Specify the URL of the Company")
arg_parser.add_argument('--dl', help="Download all APK in the current diretory", action='store_true')
args = arg_parser.parse_args()

# Get variable
main_url = args.url
download = args.dl

try:
    if main_url:
        if verify_url(main_url):
            unique_app = app_horizontal_enumeration(main_url)

            if download:
                download_app(unique_app)

        else:
            print("[!] %s is not a Google Play Store URL. Leaving ..." % main_url)

    else:
        arg_parser.print_help()

except KeyboardInterrupt:
    print("\n[x] Leaving ...")
