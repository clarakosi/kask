import os
from flask import Flask, jsonify, Response, request, abort
from semantic_version import Version
from .problems import HttpException, HttpNotFound

version = Version("1.0.0")
versioned = lambda p: "/v{}/{}".format(version.major, p.strip("/")).rstrip("/")
ENVIRONMENT = os.environ.get("ENV", default="Development")

app = Flask(__name__)
app.config.from_object("kask.Config")
app.config.from_object("kask.{0}".format(ENVIRONMENT))

KASK_STORE = app.config["KASK_STORE"]
KASK_STORE_ARGS = app.config["KASK_STORE_ARGS"]

store = KASK_STORE(*KASK_STORE_ARGS)

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
