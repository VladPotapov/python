import shelve

books = ['Pushkin', 'King', 'Po', 'Dostaevskiy']

b = shelve.open('script.dat')
b['books'] = books
b.sync()
print(b['books'])
b.close()

input('\nEnter')