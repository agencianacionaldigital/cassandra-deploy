import string
import random

from cassandra.cluster import Cluster

cluster = Cluster(['10.0.0.4'])
session = cluster.connect()
session.execute('USE cycling')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


for i in range(10000):
    race_name = id_generator()
    race_position = random.randint(1,10001)

    session.execute(
        "INSERT INTO race_winners (race_name, race_position) VALUES ('{}',{})".format(
            race_name , race_position))



