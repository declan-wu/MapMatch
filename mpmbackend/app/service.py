import uuid
from math import sin, cos, sqrt, atan2, radians

from db import DBConnection

class Service:
    def __init__(self):
        self.db = DBConnection()

    def init(self):
        for data in default_data:
            self.insert(data["user"], data["interest"], data["longitude"], data["latitude"], data["imgurl"])

    def insert(self, user, interest, longitude, latitude, imgurl):
        self.db.exec_statement("""
        INSERT INTO mapmatch.mpm_interests VALUES
        ('{}'::uuid, '{}', '{}', {}, {}, '{}')
        """.format(uuid.uuid4(), user.lower(), interest, longitude, latitude, imgurl))
        return True

    def query(self, user, interest, longitude, latitude):
        res = self.db.exec_query("""
        SELECT * FROM mapmatch.mpm_interests WHERE interests = '{}' AND user <> '{}'
        """.format(interest, user.lower()))

        result = []

        for i in range(len(res)):
            cur_long, cur_lat = res[i][3], res[i][4]
            R = 6373.0

            lat1 = radians(float(latitude))
            lon1 = radians(float(longitude))
            lat2 = radians(float(cur_lat))
            lon2 = radians(float(cur_long))

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c

            if distance <= 6.0:
                result.append((res[i][0],res[i][1],res[i][2], res[i][3], res[i][4], res[i][5]))

        return result

    def fullquery(self):
        res = self.db.exec_query("""
        SELECT * FROM mapmatch.mpm_interests
        """)

        return res
