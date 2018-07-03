def delete_an_entry():
    entry_to_delete = raw_input('Please enter the name of the person to delete: ')
    del phone_book[entry_to_delete]
    print 'Deleted entry for %s.' % entry_to_delete

phone_book = {'brandon': '263748', 'john': '23267502'}

delete_an_entry()
print phone_book