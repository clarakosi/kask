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
                       python-semantic-version
                       


For development:

    $ virtualenv -p `which python3` kask
    ...
    $ . kask/bin/activate
    $ pip install -r requirements.txt
    $ FLASK_APP=kask/index.py FLASK_DEBUG=1 flask run

