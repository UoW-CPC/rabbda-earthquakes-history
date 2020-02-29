from tinydb import TinyDB, Query
from datetime import datetime


class Database:

    @classmethod
    def queryInput(cls, yearsTempList, magnitudeOver, overwrite):
        years = []
        db = TinyDB('../yearsdb.json')
        for year in yearsTempList:
            now = str(datetime.utcnow())
            if overwrite:
                db.insert({'year': year, "magnitudeOver": magnitudeOver, 'requestDate': now})
                years = yearsTempList
            else:
                query = Query()
                record = db.search((query.year == year) & (query.magnitudeOver == magnitudeOver))
                if record == []:
                    db.insert({'year': year, "magnitudeOver": magnitudeOver, 'date': now})
                    years.append(year)
        return years
