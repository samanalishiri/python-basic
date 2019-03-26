# Saman Alishiri samanalishiri@gmail.com


class FilterList:

    def __init__(self, collection, filter_method):
        self.__collection = collection
        self.__filter_method = filter_method

    def get_original_list(self):
        return self.__collection

    def get_filtered_list(self):
        return list(filter(self.__filter_method, self.__collection))


def event_number_filter(n):
    return True if n % 2 == 0 else False
