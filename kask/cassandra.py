from cassandra.cluster import Cluster

"""
Before all make sure to create keyspace and table
ex:
    CREATE KEYSPACE IF NOT EXISTS "kask" WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
    DROP TABLE IF EXISTS kask.session;
    CREATE TABLE IF NOT EXISTS kask.session(key text, value text, PRIMARY KEY(key));
"""

cluster = Cluster()
session = cluster.connect("kask")

class CassandraStore:
    def get(self, key):
        rows = session.execute("SELECT * FROM session WHERE key=%s", (key, ))
        for session_row in rows:
            return session_row.value
        return None

    def set(self, key, value):
        session.execute("INSERT INTO session (key, value) VALUES (%s, %s)", (key, value))

    def delete(self, key):
        session.execute("DELETE FROM session WHERE key=%s IF EXISTS", (key, ))

