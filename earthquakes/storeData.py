import os


class StoreData:

    @classmethod
    def toFile(cls, eq_list, year, d):
        count = 0
        with open('../data/earthquakes{}.csv'.format(year), 'a') as writer:
            for eq in eq_list:
                count = count + 1
                eq_str = ",".join(eq)
                writer.write("%s\r\n" % (eq_str))
            print "Data for {} stored to file, records: {}".format(d, count)

    @classmethod
    def createFolder(cls):
        path = "../data/"
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed, already exist" % path)
        else:
            print ("Successfully created the directory %s " % path)
