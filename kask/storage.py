
import abc


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

