
import abc

from cassandra         import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query   import SimpleStatement


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
    def close(self):
        pass

class MockStore(Store):
    def __init__(self):
        self._values = {}

    def get(self, key):
        if key in self._values: return self._values[key]
        else: return None

    def set(self, key, value):
        self._values[key] = value

    def delete(self, key):
        if key in self._values:
            del self._values[key]

    def close(self):
        pass

class CassandraStore(Store):
    def __init__(self, keyspace=None, table=None, contacts=None):
        self.cluster = Cluster(contacts)
        self.session = self.cluster.connect()

    def get(self, key):
        pass

    def set(self, key, value):
        pass

    def delete(self, key):
        pass

    def close(self):
        self.cluster.shutdown()

    def _execute(self, query, query_args, consistency_level=ConsistencyLevel.LOCAL_QUORUM):
        pass
