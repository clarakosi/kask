import abc

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement


class Store(abc.ABC):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

    @abc.abstractmethod
    def delete(self, key):
        pass

    @abc.abstractmethod
    def clear(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass


class MockStore(Store):
    def __init__(self):
        self._values = {}

    def get(self, key):
        if key in self._values:
            return self._values[key]
        else:
            return None

    def set(self, key, value):
        self._values[key] = value

    def delete(self, key):
        if key in self._values:
            del self._values[key]

    def clear(self):
        self._values.clear()

    def close(self):
        pass


class CassandraStore(Store):
    def __init__(self, keyspace=None, table=None, contacts=None):
        self.cluster = Cluster(contacts)
        self.session = self.cluster.connect()
        self.keyspace = keyspace
        self.table = table
        self.location = "%s.%s" % (self.keyspace, self.table)

    def get(self, key):
        query = "SELECT * FROM {0} WHERE key=%s".format(self.location)
        row = self._execute(query, (key, ))

        if not row:
            return None
        return row[0].value

    def set(self, key, value):
        query = "INSERT INTO {0} (key, value) VALUES (%s, %s)".format(self.location)
        self._execute(query, (key, value))

    def delete(self, key):
        query = "DELETE FROM {0} WHERE key=%s".format(self.location)
        self._execute(query, (key, ), ConsistencyLevel.QUORUM)

    def clear(self):
        pass

    def close(self):
        self.cluster.shutdown()

    def _execute(self, query, query_args, consistency_level=ConsistencyLevel.LOCAL_QUORUM):
        statement = SimpleStatement(query, consistency_level=consistency_level)
        return self.session.execute(statement, query_args)
