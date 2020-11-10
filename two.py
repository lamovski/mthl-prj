class One:
    def __init__(self, name):
        self.name = name

class Two:
    def __init__(self, name):
        self.name = name

    def perform(self, one):
        one.name = '...'
        print(self.name, 'performed', one.name)

one = One('text')
two = Two('stuff')
print(one.name)
two.perform(one)
