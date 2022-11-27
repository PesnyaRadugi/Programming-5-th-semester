from os import path
import Strategies

class Fileservice:
    def __init__(self, data : dict):
        self.data = data
        self.counter = 0
    
    def get_strategy(self, strategy):
        return strategy.do_something(self)
            
def Help():
        return ( '''
            save - Save filepath
            get - Get path
            del - Delete filepath
            get_list - Get list of filepaths
            change_id - change id of filepath
            backup - Save progress between sessions
            quit - Shup down
        ''')

def Initialize():
    
    if path.exists('save_file.txt'):
        pass
    else:
        open('save_file.txt', 'w+', encoding='utf-8')
    
    while True:
        usr_input = input('Would you like to restore your last saved session session ? y/n\n')
        if usr_input == 'y':
            save_file = open('save_file.txt', 'r', encoding='utf-8')
            try:
                data = eval(save_file.read())
                return Fileservice(data)
            except:
                print('Seems like your save file is empty, creating new.....')
                return Fileservice({})
        elif usr_input == 'n':
            return Fileservice({})
        else:
            print('Invalid command try again')

def Navigate_menu(service : Fileservice): 
    while True:
        usr_input = input('>').lower()
        match usr_input:
            case 'save':
                service.get_strategy(Strategies.file_saver)
            case 'get':
                print(service.get_strategy(Strategies.file_getter))
            case 'del':
                service.get_strategy(Strategies.file_deleter)
            case 'get_list':
                print(service.get_strategy(Strategies.list_getter))
            case 'change_id':
                service.get_strategy(Strategies.id_changer)
            case 'backup':
                service.get_strategy(Strategies.backuper)
            case 'help':
                print(Help())
            case 'quit':
                break
            case _:
                print('Invalid command, if you stuck use "help" to see list of commands')
                
def Main():
    print('Hello write "help" to see list of commands')
    Navigate_menu(Initialize())
    
if __name__ == '__main__':
    Main()