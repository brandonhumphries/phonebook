def look_up_an_entry():
    option1_prompt = raw_input('What is the name of the person? ')
    while option1_prompt not in phone_book:
        print 'Name not found, please enter name of the person lised in the phonebook. Otherwise, please add as a new entry. '
        option1_prompt = raw_input('What is the name of the person? ')
    if option1_prompt in phone_book:
        found_entry_message = 'Found entry for %s: %s' % (option1_prompt, phone_book[option1_prompt])
        print found_entry_message
    #phonebook()

phone_book = {'brandon': '2357098', 'john': '2830974'}

look_up_an_entry()