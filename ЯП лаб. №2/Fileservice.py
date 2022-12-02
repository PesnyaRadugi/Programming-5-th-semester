from os import path


class Fileservice:
    def __init__(self, data):
        self.data = data
        self.counter = 0
    
    def save_file(self, filename):
        while True:
            id = self.counter
            self.counter += 1
            if id in self.data.keys():
                continue
            else:
                self.data[id] = filename 
                print(f'File path saved with id = {self.counter - 1}')
                break
        return id
    
    def get_file(self, id):
        try:
            return self.data[id]
        except:
            raise Exception('File not found')
        
    def delete_file(self, id):
        try:
            self.data.pop(id)
            self.counter = id
            print(f'Successfully deleted file with id = {id}')
        except:
            raise Exception('No such id')    

    def change_id(self, old_id, new_id):
        self.data[new_id] = self.data[old_id]
        self.delete_file(old_id)
        print(f'Changed id from {old_id} to {new_id}')
    
    def get_list(self, lst_of_id):
        lst_of_paths = []
        for i in lst_of_id:
            lst_of_paths.append(self.get_file(i))
        
        return lst_of_paths
        
    def backup(self, data):
        try:
            save_file = open('save_file.txt', 'w', encoding='utf-8')
            save_file.write(str(data))
            print('Backup successfull')
        except:
            raise Exception('Nothing to save')
    
    def from_backup(self):
        usr_input = input('Would you like to restore your last saved session session ? y/n\n')
        if usr_input == 'y':
            save_file = open('save_file.txt', 'r', encoding='utf-8')
            try:
                self.data = eval(save_file.read())
            except:
                raise Exception('No data / save file is missing')
        elif usr_input == 'n':
            return
        else:
            print('Invalid command try again')
     
def Help():
        return ( '''
            save - Save filepath
            get - Get path
            del - Delete filepath
            get_list - Get list of filepaths
            change_id - change id of filepath
            backup - Save progress between sessions
            restore - Restore session from save file
            quit - Shup down
        ''')

def Initialize():
    if path.exists('save_file.txt'):
        pass
    else:
        open('save_file.txt', 'w+', encoding='utf-8')   
    return Fileservice({})


def Navigate_menu(service : Fileservice): 
    while True:
        usr_input = input('>').lower()
        match usr_input:
            case 'save':
                service.save_file(input('Enter path\n'))
            case 'get':
                print(service.get_file(int(input('Enter id\n'))))
            case 'del':
                service.delete_file(int(input("Enter id you'd like to delete\n")))
            case 'get_list':
                print(service.get_list([int(i) for i in input('Enter ids separated by space:\n').split()]))
            case 'change_id':
                service.change_id(int(input('Enter id of file you want to change: ')), int(input('Enter new id: ')))
            case 'backup':
                service.backup(service.data)
            case 'restore':
                service.from_backup()
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