def phonebook():
    print 'Electronic Phone Book'
    print '====================='
    print '1. Look up an entry'
    print '2. Set an entry'
    print '3. Delete an entry'
    print '4. List all entries'
    print '5. Quit'
    option_choice = raw_input('What do you want to do (1-5)? ')
    return option_choice

phonebook()
