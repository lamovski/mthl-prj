class Ticket:
    ticket_class = 2
    cost = 3.50

    def __init__(self, where_to, where_from, time, train_num):
        self.where_from = where_from
        self.where_to = where_from
        self.time = time
        self.train_num = train_num

    def aboot(self):
        print(self.where_to, self.where_from, self.time, self.train_num, self.cost)


class Passenger:
    cash = 3.50

    def buy(self, where_to, where_from, time, train_num):
        ticket = Ticket(where_to, where_from, time, train_num)
        self.ticket = ticket
        self.cash-=ticket.cost

man = Passenger()
man.buy('Buffalo', 'NY', '12:34', '65536')
print(man.cash)
print(man.ticket.aboot())
