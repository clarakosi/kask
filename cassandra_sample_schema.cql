-- -*- mode: sql -*-

CREATE KEYSPACE IF NOT EXISTS mw WITH
    replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS mw.sessions (key blob PRIMARY KEY, value blob);
