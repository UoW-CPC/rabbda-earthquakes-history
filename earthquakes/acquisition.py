import csv
import eventlet
import requests
from datetime import timedelta, date


class Acquisition:

    @classmethod
    def request(cls, year, magnitudeOver):
        eventlet.monkey_patch()
        with eventlet.Timeout(5):
            try:
                firstDate = date(year, 1, 1)
                lastDate = date(year, 12, 31)
                for d in dateRange(firstDate, lastDate):
                    start = d.strftime("%Y-%m-%d") + "T00:00:00.000Z"
                    end = (d + timedelta(days=1)).strftime("%Y-%m-%d") + "T00:00:00.000Z"
                    print start + " " + end

                with requests.Session() as s:
                    download = s.get(
                        "https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime={}&endtime={}&minmagnitude={}".format(
                            start, end, magnitudeOver))
                    decoded_content = download.content.decode('utf-8')
                    eq_csv = csv.reader(decoded_content.splitlines(), delimiter=',')
                    eq_list = list(eq_csv)
                    return eq_list

            except:
                print("Request error")


def dateRange(firstDate, lastDate):
    for n in range(int ((lastDate - firstDate).days)):
        yield firstDate + timedelta(n)
