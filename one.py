class Bruh:
    bruh_amount = 0
    bruh_list = []

    def __init__(self, name):
        self.name = name

    def add_bruh(self, bruh):
        self.bruh_list.append(bruh)
        bruh.bruh_list.append(self)

    def say(self):
        print('bruh')

joe = Bruh('joe')
jack = Bruh('jack')
jack.add_bruh(joe)
joe.say()

print(jack.bruh_list)
print(joe.bruh_list)
