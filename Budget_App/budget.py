class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __repr__(self):
        str_print = self.name.center(30, "*")+'\n'

        for entry in self.ledger:
            name_format = entry['description'][:23]

            str_print += name_format + \
                str(entry['amount']).rjust(30-len(name_format))+'\n'

        str_print += 'Total: '+str(self.get_balance())+'\n'
        return str_print

    def deposit(self, amount, description=''):
        dep = {'amount': amount, 'description': description}
        self.ledger.append(dep)

    def check_funds(self, amount):
        bal = self.get_balance()
        if bal > amount:
            return False
        else:
            return True

    def get_balance(self):
        balance = sum([self.ledger[i]['amount']
                       for i in range(0, len(self.ledger))])
        return balance

    def withdraw(self, amount, description=''):
        if self.check_funds == True:
            pass
        else:
            wit = {'amount': -(amount), 'description': description}
            self.ledger.append(wit)

    def transfer(self, amount, cat_name):
        new_cat = Category(cat_name)
        self.withdraw(amount, description=f'Transfer to {cat_name.name}')
        if self.check_funds == False:
            new_cat.deposit(amount, description=f'Transfer from {self.name}')


def create_spend_chart(categories):
    cat_names = {}

    for category in categories:
        for entry in category.ledger:
            tot_withdraws = 0
            tot_deposits = 0
            if entry['amount'] < 0:
                tot_withdraws += entry['amount']
            else:
                tot_deposits += entry['amount']

        percent_spent = round((tot_deposits/tot_withdraws), 1)*100
        cat_name = category.name.split()

        cat_names.setdefault(cat_name, [range(0, percent_spent+10)])

    full_str_percen = ''
    full_str_name = ''
    for key, value in cat_names.getitems():
        name_chr = cat_names[key].split()
        percen = cat_names[value]
        for i in range(100, -10, -10):
            if i not in percen:
                full_str += i.rjust(3)+'| '+'\n'
            else:
                full_str += i.rjust(3)+'| '+'o'
