phone_book = {
    'brandon': '29709462',
    'john': '07284601',
    'alex': '864609713'
    }

def main_menu():
    print 'Electronic Phone Book'
    print '====================='
    print '1. Look up an entry'
    print '2. Set an entry'
    print '3. Delete an entry'
    print '4. List all entries'
    print '5. Quit'
    #option_choice = raw_input('What do you want to do (1-5)? ')
    #return option_choice

def look_up_an_entry():
    option1_prompt = raw_input('What is the name of the person? ')
    if option1_prompt in phone_book:
        found_entry_message = 'Found entry for %s: %s' % (option1_prompt, phone_book[option1_prompt])
        print found_entry_message
    else:
        print '\nName not found. Returning to main menu.\n'

def set_an_entry():
    name_prompt = raw_input('What is the name of the person to be added? ')
    number_prompt = raw_input('What is the phone number of the person to be added? ')
    phone_book[name_prompt] = number_prompt
    print 'Entry stored for %s.' % (name_prompt)

def delete_an_entry():
    entry_to_delete = raw_input('Please enter the name of the person to delete: ')
    del phone_book[entry_to_delete]
    print 'Deleted entry for %s.' % entry_to_delete

def list_all_entries():
    for key in phone_book:
        print 'Found entry for %s: %s' % (key, phone_book[key])

def goodbye():
    print 'Goodbye'