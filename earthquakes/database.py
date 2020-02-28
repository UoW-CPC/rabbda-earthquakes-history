from tinydb import TinyDB, Query
from datetime import datetime


class Database:

    @classmethod
    def validateYears(cls, yearsTempList, overwrite):
        years = []
        db = TinyDB('../yearsdb.json')
        for year in yearsTempList:
            now = str(datetime.utcnow())
            if overwrite:
                db.insert({'year': year, 'date': now})
                years = yearsTempList
            else:
                query = Query()
                record = db.search(query.year == year)
                if record == []:
                    db.insert({'year': year, 'date': now})
                    years.append(year)
        return years
