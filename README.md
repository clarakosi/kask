kask
====
Kask is a multi-master key-value data store built on Apache Cassandra.


Requirements
------------

Kask's dependency list is meant to be satisfiable entirely from
packages in Debian stable (Stretch at the time of writing).

    $ sudo apt install python-flask \
                       python-cassandra \
                       python-prometheus-client \
                       python-semantic-version \
                       black
                       


Development
-----------
The development assumes that Cassandra is running and that  `dev_keyspace.dev_table` exits.
If not you can create the keyspace and table using the following commands in cqlsh:
    
    $ CREATE KEYSPACE dev_keyspace WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
    $ CREATE TABLE dev_keyspace.dev_table (key text PRIMARY KEY, value text)
    
To start flask:

    $ virtualenv -p `which python3` kask
    ...
    $ . kask/bin/activate
    $ pip install -r requirements.txt
    $ FLASK_APP=kask/index.py FLASK_DEBUG=1 flask run 
    
    $ # ...or alternatively...
    $ gunicorn --reload -b 0.0.0.0:5000 kask.index:app

    

Reformating code using [black](https://pypi.org/project/black) (i.e. to *blacken*):

    $ black .

Tests
-----------
For unit tests:

    $ ENV=MockTesting python -m unittest tests/test*

For functional tests, you must first have Cassandra running. Then simply run:
    
    $ ENV=CassandraTesting python -m unittest tests/functional_tests/test*

