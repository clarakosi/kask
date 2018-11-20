import kask.storage

class Config(object):
    DEBUG = True

class CassandraTesting(object):
    KASK_STORE = kask.storage.CassandraStore
    KASK_STORE_ARGS = []

class MockTesting(object):
    KASK_STORE = kask.storage.MockStore
    KASK_STORE_ARGS = []

class Development(object):
    KASK_STORE = kask.storage.CassandraStore
    KASK_STORE_ARGS = ["dev_keyspace", "dev_table"]
