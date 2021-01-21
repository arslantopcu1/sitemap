#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import logging
from pysitemap import crawler

parser = argparse.ArgumentParser(description='Python SiteMap Crawler')
parser.add_argument('--domain', default="https://www.lipsum.com", help="File extension to skip")
parser.add_argument('--task', type=int, default=10, help="File extension to skip")

arg = parser.parse_args()

#logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s')
#logging.info("Start the crawling process domain: %s", arg.domain)

if __name__ == '__main__':
    # root_url = sys.argv[1]
    crawler(arg.domain, out_file='sitemap.xml', maxtasks= arg.task)
