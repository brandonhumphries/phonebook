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

def set_an_entry():
    option2_name_prompt = raw_input('What is the name of the person to be added? ')
    option2_number_prompt = raw_input('What is the phone number of the person to be added? ')
    phone_book[option2_name_prompt] = option2_number_prompt
    print 'Entry stored for %s.' % (option2_name_prompt)
    return phone_book

phone_book = {}
print set_an_entry()