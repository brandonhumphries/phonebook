def list_all_entries():
    for key in phone_book:
        print 'Found entry for %s: %s' % (key, phone_book[key])

phone_book = {'brandon': '23857203', 'john': '23802397', 'mike': '283075', 'alex': '20974'}

list_all_entries()