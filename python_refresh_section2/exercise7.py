class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        another_store = cls(store.name)
        return '{} - franchise'.format(another_store.name)

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return '{0}, total stock price: {1}'.format(store.name, int(store.stock_price()))


store = Store('Test')
store2 = Store('Amazon')
store2.add_item("Keyboard", 160)

Store.franchise(store) # returns a Store with name "Test - franchise"
Store.franchise(store2) # returns a Store with name "Amazon - franchise"

Store.store_details(store) # returns "Test, total stock price: 0"
Store.store_details(store2) # returns "Amazon, total stock price: 0"
