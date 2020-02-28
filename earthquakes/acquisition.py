import csv
import eventlet
import requests
from datetime import timedelta, date


class Acquisition:

    @classmethod
    def request(cls, start, end, magnitudeOver):
        eventlet.monkey_patch()
        with eventlet.Timeout(10):
            try:
                with requests.Session() as s:
                    download = s.get(
                        "https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime={}&endtime={}&minmagnitude={}".format(
                            start, end, str(magnitudeOver)))
                    decoded_content = download.content.decode('utf-8')
                    eq_csv = csv.reader(decoded_content.splitlines(), delimiter=',')
                    eq_list = list(eq_csv)
                    return eq_list
            except Exception as error:
                print"Request error: ", error
