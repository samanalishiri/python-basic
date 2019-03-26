from step_b_collection_project.collections import List


class Console:
    START_LINE = '-> '
    BLOCK = '**'

    def __init__(self):
        self.collection_list = List([])
        self.life = True
        self.commands = dict({
            'help': self.help,
            'append': self.append,
            'remove': self.remove,
            'sort': self.sort,
            'origin': self.origin,
            'exit': self.end,
        })

    def help(self):
        print('['.__add__(' , '.join(self.commands.keys())).__add__(']'))

    def append(self):
        append = True
        self.print_message('enter number or sequence of number with comma separate')
        while append:
            value = input(Console.START_LINE)
            try:
                array = value.split(',')
                for n in array:
                    self.collection_list.append(int(n))
            except ValueError:
                print('end of append')
                append = False

    def remove(self):
        remove = True
        self.print_message('enter number or sequence of number with comma separate')
        while remove:
            value = input(Console.START_LINE)
            try:
                array = value.split(',')
                for n in array:
                    self.collection_list.remove(int(n))
            except ValueError:
                print('end of remove')
                remove = False

    def sort(self):
        self.collection_list.sort()
        print(self.collection_list.sorted())

    def origin(self):
        print(self.collection_list.origin())

    def end(self):
        self.life = False

    @staticmethod
    def print_message(message):
        print('%s '.__add__(message).__add__(' %s') % (Console.BLOCK, Console.BLOCK))

    def execute(self):
        self.print_message('enter command, help')
        while self.life:
            try:
               self.commands[input('-> ')]()
            except Exception:
                print('invalid command!')


if __name__ == '__main__':
    Console().execute()