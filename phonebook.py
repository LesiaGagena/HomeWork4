contacts = {}  # added missing dictionary declaration

# decorator
def input_error(func):
    def inner(name, phone):
        try:
            result = func(name, phone)
            return result
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Please give me name and phone number separated by space"
        except IndexError:
            return "Please provide name or name and phone number separated by space"
    return inner

def exit_test(_):
    return 

def hello_users(_):
    print("How can I help you?")

@input_error
def add_contact(name, phone):  # added  to accept variable number of arguments
    contacts[name] = phone
    return f"{name}'s phone number {phone} added"

def unknown_command(_):
    print('Unknown command') 

@input_error
def change_contact(name, phone):  #
    old_phone = contacts[name]
    contacts[name] = phone
    return f"{name}'s old phone number {old_phone} changed to {phone}"

def show_phone(name, phone):  # changed function signature to accept variable number of arguments
    if not contacts:
        return "No contacts found"
    search_name = name[0]
    phone = contacts.get(search_name)
    if phone:
        return f'Name {search_name}: phone {phone}'
    return "Contact not found"

def show_all(name, phone):  # changed function signature to accept variable number of arguments
    if not contacts:
        return "No contacts found"
    result = ''
    for name, phone in contacts.items():
        result += f'Name {name}: phone {phone} \n'
    return result

HANDLERS = {
    'hello': hello_users,
    'add': add_contact,
    'change': change_contact,
    'show all': show_all,
    'exit': exit_test,
    'goodbye': exit_test,  # corrected spelling
    'close': exit_test
}

def parse_input(user_input):
    command_name, name, phone = user_input.split()
    command_name = command_name.lstrip()

    try:
        handler = HANDLERS[command_name.lower()]
    except KeyError:
        if args:
            command_name = command_name + ' ' + args[0]
            args = args[1:]
        handler = HANDLERS.get(command_name.lower(), unknown_command)
    return handler, name, phone

def main():
    while True:
    
        print('Please input command, name and phone. For example: add Lesia 033-332-2233')
        user_input = input('')
        handler, name, phone = parse_input(user_input)
        result = handler(name, phone)
        if not result:
            print('input true args')  # corrected typo
            break
        print(result)

if __name__ == "__main__":
    main()
