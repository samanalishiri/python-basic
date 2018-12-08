from collections import ChainMap


# Saman Alishiri samanalishiri@gmail.com
class Chain:
    def __init__(self):
        self.__chain = None

    def forward(self, val):
        self.__chain = ChainMap() if self.__chain is None else self.__chain.new_child()
        self.__chain['node'] = val
        return self

    def back(self):
        self.__chain = self.__chain.parentd
        return self

    def collect(self):
        return self.__chain.maps

    def iterate(self):
        for node in self.__chain.maps:
            yield node['node']
