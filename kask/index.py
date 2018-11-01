
from flask            import Flask, jsonify, Response, request, abort
from semantic_version import Version
from .problems        import HttpException, HttpNotFound
from .storage         import MockStore


version = Version("1.0.0")
versioned = lambda p: "/v{}/{}".format(version.major, p.strip('/')).rstrip('/')

app = Flask(__name__)
app.config.from_object("kask.Config")
store = MockStore()


@app.route(versioned("/<key>"), methods=["GET"])
def get(key):
    # TODO: exception handling
    value = store.get(key)
    if not value:
        raise HttpNotFound(versioned(key))
    return jsonify(dict(value=value))

@app.route(versioned("/<key>"), methods=["PUT"])
def set(key):
    # TODO: exception handling
    json = request.get_json() or abort(400)
    # TODO: validate schema(?)
    store.set(key, json["value"])
    return Response("", status=201, mimetype="application/json")

@app.route(versioned("/<key>"), methods=["DELETE"])
def delete(key):
    # TODO: exception handling
    store.delete(key)
    return jsonify(), 204

@app.errorhandler(HttpException)
def handle_http_error(error):
    return error.response()

