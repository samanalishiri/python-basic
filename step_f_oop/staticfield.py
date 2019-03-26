
class StaticField:
    number_of_instance = 0

    def __init__(self):
        StaticField.number_of_instance += 1
