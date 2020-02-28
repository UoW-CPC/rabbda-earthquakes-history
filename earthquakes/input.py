import sys, getopt
from datetime import datetime


class Input:

    @classmethod
    def evaluate(cls, inputArgs):
        print inputArgs
        options = "y:f:t:o"
        longOptions = ["year=", "from-year=", "to-year=", "overwrite"]
        try:
            opts, args = getopt.getopt(inputArgs, options, longOptions)
        except getopt.GetoptError as err:
            print (str(err))
            sys.exit(2)

        yearFlag = False
        yearArg = None
        fromYearFlag = False
        fromYearArg = None
        toYearFlag = False
        toYearArg = None
        overwriteFlag = False

        for opt, arg in opts:
            if opt in ("-y", "--year"):
                if yearFlag:
                    cls.notUniqueArg()
                else:
                    yearFlag = True
                    yearArg = arg
            elif opt in ("-f", "--from-year"):
                if fromYearFlag:
                    cls.notUniqueArg()
                else:
                    fromYearFlag = True
                    fromYearArg = arg
            elif opt in ("-t", "--to-year"):
                if toYearFlag:
                    cls.notUniqueArg()
                else:
                    toYearFlag = True
                    toYearArg = arg
            elif opt in ("-o", "--overwrite"):
                if overwriteFlag:
                    cls.notUniqueArg()
                else:
                    overwriteFlag = True

        if fromYearFlag and toYearFlag and not yearFlag:
            print "Accepted input parameters. From - To"
        elif not fromYearFlag and not toYearFlag and yearFlag:
            print "Accepted input parameter. Year"
        else:
            print "Input Parameters Error.\r\n" \
                  "You must pass parameters in one of the following formats:\r\n" \
                  "Example with a range of values:       '--from-year=2010 --to-year=2020'\r\n" \
                  "Example with a list of unique values: '--year=2010,2011,2012'\r\n" \
                  "Exiting the application.."
            sys.exit(2)
        if overwriteFlag:
            print "Overwrite data is enabled"

        yearList = cls.toList(yearArg)
        fromYearInt = cls.validateYear(fromYearFlag)
        toYearInt = cls.validateYear(toYearArg)
        return fromYearInt,toYearInt

    @classmethod
    def notUniqueArg(cls):
        print "Input Error. Can't pass one argument twice. Exiting the application.."
        sys.exit(2)

    @classmethod
    def toList(cls):
        print "hello"

    @classmethod
    def validateYear(cls, arg):
        now = datetime.utcnow()
        currentYear = now.year
        try:
            year = int(arg)
            if 1900 <= year <= currentYear:
                return year
            else:
                sys.exit(2)
        except:
            print (
                "invalid year input, value: '{}'. You can only pass year values from '1900' to '{}'. Exciting the application..".format(
                    arg, currentYear))
            sys.exit(2)
