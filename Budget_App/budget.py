class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __repr__(self):
        str_print = self.name.center(30, "*")+'\n'

        for entry in self.ledger:
            name_format = entry['description'][:23]

            str_print += name_format + \
                "{:.2f}".format(entry['amount']).rjust(
                    30-len(name_format))+'\n'

        str_print += 'Total: '+str(self.get_balance())
        return str_print

    def deposit(self, amount, description=''):
        dep = {'amount': amount, 'description': description}
        self.ledger.append(dep)

    def check_funds(self, amount):
        bal = self.get_balance()
        if bal < amount:
            return False
        else:
            return True

    def get_balance(self):
        balance = sum([self.ledger[i]['amount']
                       for i in range(0, len(self.ledger))])
        return balance

    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == False:
            return False
        else:
            wit = {'amount': -(amount), 'description': description}
            self.ledger.append(wit)
            return True

    def transfer(self, amount, cat_name):
        if self.check_funds(amount) == False:
            return False
        else:
            self.withdraw(amount, description=f'Transfer to {cat_name.name}')
            cat_name.deposit(amount, description=f'Transfer from {self.name}')
            return True


def create_spend_chart(categories):
    percen_dict = {str(num): str(num).rjust(
        3)+'| ' for num in range(100, -10, -10)}
    max_cat_name = max([category.name
                        for category in categories], key=len)
    len_max_cat_name = len(max_cat_name)
    name_dict = {index: '     ' for index in range(0, len_max_cat_name)}
    horiz_line = '    '+'-'*(1+(len(categories)*3))

    cat_withdraws = []
    for category in categories:
        tot_withdraws = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                tot_withdraws += -(entry['amount'])
        cat_withdraws.append(tot_withdraws)

        cat_name = [ch for ch in category.name]
        for i in range(0, len_max_cat_name):
            if i <= len(cat_name)-1:
                name_dict[i] += cat_name[i]+'  '
            else:
                name_dict[i] += '   '

    cat_percen = [round((cat/(sum(cat_withdraws)))*100)
                  for cat in cat_withdraws]

    for cat in cat_percen:
        for percen in range(100, -10, -10):
            if percen <= cat:
                percen_dict[str(percen)] += 'o  '
            else:
                percen_dict[str(percen)] += '   '

    mas_str = 'Percentage spent by category\n'
    for value in percen_dict.values():
        mas_str += value+'\n'
    mas_str += horiz_line+'\n'
    for key, value in name_dict.items():
        if key == len_max_cat_name-1:
            mas_str += value
        else:
            mas_str += value+'\n'
    return mas_str
