# -*- coding: utf-8 -*-
import scrapy
import json

from urlparse import urlparse

class SecuritiesSpider(scrapy.Spider):
    name = 'securities'
    allowed_domains = ['http://www.planspiel-boerse.com/bceeluxembourg/_js_DS/1/wertpapiere.json?_=25147811']
    start_urls = ['http://www.planspiel-boerse.com/bceeluxembourg/_js_DS/1/wertpapiere.json?_=25147811/']

    def parse(self, response):
	parsed_json = json.loads(response.text)

	for item in parsed_json['wp']:
		info = {
			'name' : item[1],		
			'id' : urlparse(item[2]).query[14:],
			'type' : item[5],
		}

		yield info
