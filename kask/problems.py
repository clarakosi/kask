"""
Exceptions in support of RFC7807 HTTP responses (https://tools.ietf.org/html/rfc7807)
"""

from abc import ABCMeta, abstractmethod
from flask import jsonify


class HttpException(Exception):
    __metaclass_ = ABCMeta

    @property
    @abstractmethod
    def type(self):
        pass

    @property
    @abstractmethod
    def status(self):
        pass

    @property
    @abstractmethod
    def title(self):
        pass

    @property
    @abstractmethod
    def detail(self):
        pass

    @property
    @abstractmethod
    def instance(self):
        pass

    def __init__(self, *args, **kwargs):
        raise NotImplementedError()

    def jsonify(self):
        return jsonify(
            dict(type=self.type, title=self.title, detail=self.detail, instance=self.instance)
        )

    def response(self):
        return self.jsonify(), self.status


class HttpNotFound(HttpException):
    @property
    def type(self):
        return "https://www.mediawiki.org/wiki/probs/not-found"

    @property
    def status(self):
        return 404

    @property
    def title(self):
        return "Not found"

    @property
    def detail(self):
        return "The requested resource was not found"

    @property
    def instance(self):
        return self._instance

    def __init__(self, instance):
        super(HttpException, self).__init__(self, instance)
        self._instance = instance


class HttpBadRequest(HttpException):
    pass


class HttpNotAuthorized(HttpException):
    pass


class HttpInternalServerError(HttpException):
    pass
