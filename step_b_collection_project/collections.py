class List:

    def __init__(self, array):
        self._elements = array
        self._sort_elements = []

    def append(self, e):
        self._elements.append(e)

    def remove(self, e):
        if e in self._elements:
            self._elements.remove(e)

    def sort(self, key=None):
        if key is None:
            self._sort_elements = sorted(self._elements, key=lambda e: e)
            return self._sort_elements
        else:
            self._sort_elements = sorted(self._elements, key=lambda e: self._elements[key])
            return self._sort_elements

    def origin(self):
        return self._elements

    def sorted(self):
        return self._sort_elements
