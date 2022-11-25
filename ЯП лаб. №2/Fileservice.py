class Fileservice:
    def __init__(self):
        self.data = {}
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
            return 'File not found'
        
    def delete_file(self, id):
        self.data.pop(id)
        self.counter = id
        
    def change_id(self, old_id, new_id):
        self.data[new_id] = self.data.pop(old_id)
        self.counter = old_id
        print(f'Changed id from {old_id} to {new_id}')
    
    def get_list(self, lst_of_id):
        lst_of_paths = []
        for i in lst_of_id:
            lst_of_paths.append(self.get_file(i))
        
        return lst_of_paths
        
    def backup(self, data):
        try:
            self.data = data
            self.counter = max(data.keys())
            print('Backup successfull')
        except:
            print('Nothing to save')
            
def Help():
        print( '''
            save - Save filepath
            get - Get path
            del - Delete filepath
            get_list - Get list of filepaths
            change_id - change id of filepath
            backup - Make backup
            quit - Shup down
        ''')

def Navigate_menu(service : Fileservice): 
    while True:
        usr_input = input('>').lower()
        if usr_input == 'save':
            service.save_file(input('Enter path\n'))
        elif usr_input == 'get':
            print(service.get_file(int(input('Enter id\n'))))
        elif usr_input == 'backup':
            service.backup(service.data)
        elif usr_input == 'del':
            print(service.delete_file(int(input('Enter id\n'))))
        elif usr_input == 'change_id':
            service.change_id(int(input('Enter id of file you want to change: ')), int(input('Enter new id: ')))
        elif usr_input == 'get_lst':
            print(service.get_list([int(i) for i in input('Enter ids separated by space: ').split()]))
        elif usr_input == 'help':
            Help()
        elif usr_input == 'quit':
            break
        else:
            print('Invalid command, if you stuck use "help" to see list of commands')

def Main():
    print('Hello')
    Navigate_menu(service = Fileservice())
        
    
if __name__ == '__main__':
    Main()