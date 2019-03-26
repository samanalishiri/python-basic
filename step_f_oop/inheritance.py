class Programmer:
    def __init__(self, lang, framework):
        self.lang = lang
        self.framework = framework

    def __str__(self):
        return '{}:{}'.format(self.lang, self.framework)


class JavaProgrammer(Programmer):
    def __init__(self, framework):
        super().__init__('Java', framework)


