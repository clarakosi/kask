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
In a nutshell:

    $ virtualenv -p `which python3` kask
    ...
    $ . kask/bin/activate
    $ pip install -r requirements.txt
    $ FLASK_APP=kask/index.py FLASK_DEBUG=1 flask run
    $ # ...or alternatively...
    $ gunicorn3 --reload -b 0.0.0.0:5000 kask.index:app

Reformating code using [black](https://pypi.org/project/black) (i.e. to *blacken*):

    $ black .

