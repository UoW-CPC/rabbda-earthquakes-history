import sys
import time
from datetime import datetime, timedelta

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
    print "Data acquisition starts"
    print "Requesting earthquakes data with magnitude over {}, for years: {}".format(magnitudeOver, years)
    for year in years:
        print year
        eq_list_raw = Acquisition.request(year,magnitudeOver)
        eq_list_temp = Preprocessing.cleanHeaders(eq_list_raw)
        eq_list = Preprocessing.splitDateTime(eq_list_temp)
        Store.toFile(eq_list,year)
        print "Data acquisition ended"


if __name__ == "__main__":
    main()
