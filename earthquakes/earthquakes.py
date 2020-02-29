import sys
from datetime import timedelta, date

from input import Input
from database import Database
from acquisition import Acquisition
from preprocessing import Preprocessing
from storeData import StoreData
from hdfs import HDFS


def main():
    inputArgs = sys.argv
    args = inputArgs[1:]
    yearsTempList, magnitudeOver, overwrite = Input.getValues(args)
    years = Database.queryInput(yearsTempList, magnitudeOver, overwrite)
    StoreData.createFolder()
    print "Requesting earthquakes data with magnitude over {}, for years: {}".format(magnitudeOver, years)
    for year in years:
        print "Processing year: ", year
        print "Data acquisition starts"
        firstDate = date(year, 1, 1)
        lastDate = date(year, 12, 31)
        for d in dateRange(firstDate, lastDate):
            start = d.strftime("%Y-%m-%d") + "T00:00:00.000Z"
            end = (d + timedelta(days=1)).strftime("%Y-%m-%d") + "T00:00:00.000Z"
            try:
                eq_list_raw = Acquisition.request(start, end, magnitudeOver)
                eq_list_temp = Preprocessing.cleanHeaders(eq_list_raw)
                eq_list = Preprocessing.splitDateTime(eq_list_temp)
                StoreData.toFile(eq_list, year, d,magnitudeOver)
            except Exception as error:
                print "Error while processing a request:", error
        print "Data acquisition ended"
        path = HDFS.getPath()
        HDFS.put('../data/earthquakes{}mag{}.csv'.format(year, magnitudeOver), path)


def dateRange(firstDate, lastDate):
    for n in range(int((lastDate - firstDate).days)):
        yield firstDate + timedelta(n)


if __name__ == "__main__":
    main()
