import os


class Store:

    @classmethod
    def toFile(cls, eq_list,year):
        cls.createFolder()
        cls.createFile(year)
        count = 0
        with open('../data/earthquakes{}.csv'.format(year), 'a') as writer:
            for eq in eq_list:
                count = count + 1
                eq_str = ",".join(eq)
                writer.write("%s\r\n" % (eq_str))
            print "Single date data stored to file, records: ",count

    @classmethod
    def createFile(cls,year):
        with open('../data/earthquakes{}.csv'.format(year), 'w') as writer:
            writer.write("")

    @classmethod
    def createFolder(cls):
        path = "../data/"
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed, already exist" % path)
        else:
            print ("Successfully created the directory %s " % path)
