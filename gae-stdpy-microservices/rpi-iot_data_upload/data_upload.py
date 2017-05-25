#!/usr/bin/env python

"""data_upload.py: Upload fake IoT data to online services"""

import requests
import random
import time
import logging

SLEEP_TIME = 2      # Sleep time in seconds


def parse_urls():
	with open('target_web_apps_ids.txt', 'r') as f:
		urls = f.read().split('\n')

	# return ['http://iot-ingest.' + u + '.appspot.com/api/v1/new_data' for u in urls if u]
	return ['http://localhost:8080/api/v1/new_data' for u in urls if u]


def main():
	while True:
		urls = parse_urls()

		data = {'device_id': str(random.randint(1, 10)),
		        'data_value': str(random.randint(0, 1000))}

		for u in urls:
			r = requests.put(u, data=data)

			res = 'URL: {}\tStatus: {}\tResponse: {}\n-  Device ID: {} \tData: {}'.format(r.url,
			                                                                              r.status_code,
			                                                                              r.text.encode('utf-8'),
			                                                                              data.get('device_id'),
			                                                                              data.get('data_value'))
			print(res)

		time.sleep(SLEEP_TIME)


if __name__ == '__main__':
	main()
