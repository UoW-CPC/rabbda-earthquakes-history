import sys
from datetime import timedelta, date

from input import Input
from database import Database
from acquisition import Acquisition
from preprocessing import Preprocessing
from store import Store


def main():
    inputArgs = sys.argv
    args = inputArgs[1:]
    yearsTempList, magnitudeOver, overwrite = Input.getValues(args)
    years = Database.validateYears(yearsTempList, magnitudeOver, overwrite)
    Store.createFolder()
    print "Data acquisition starts"
    print "Requesting earthquakes data with magnitude over {}, for years: {}".format(magnitudeOver, years)
    for year in years:
        print year
        firstDate = date(year, 1, 1)
        lastDate = date(year, 12, 31)
        for d in dateRange(firstDate, lastDate):
            start = d.strftime("%Y-%m-%d") + "T00:00:00.000Z"
            end = (d + timedelta(days=1)).strftime("%Y-%m-%d") + "T00:00:00.000Z"
            try:
                eq_list_raw = Acquisition.request(start, end, magnitudeOver)
                eq_list_temp = Preprocessing.cleanHeaders(eq_list_raw)
                eq_list = Preprocessing.splitDateTime(eq_list_temp)
                Store.toFile(eq_list, year,d)
            except Exception as error:
                print "Error while processing a request:",error

        print "Data acquisition ended"


def dateRange(firstDate, lastDate):
    for n in range(int((lastDate - firstDate).days)):
        yield firstDate + timedelta(n)


if __name__ == "__main__":
    main()
