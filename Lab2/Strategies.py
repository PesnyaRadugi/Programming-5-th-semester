from Fileservice import Fileservice


class i_strategy:
    def do_something(service : Fileservice):
        pass

class file_saver(i_strategy):
    def do_something(service: Fileservice):
        filename = input('Enter path\n')
        while True:
            id = service.counter
            service.counter += 1
            if id in service.data.keys():
                continue
            else:
                service.data[id] = filename 
                print(f'File path saved with id = {service.counter - 1}')
                break
            
class file_getter(i_strategy):
    def do_something(service: Fileservice):
        id = int(input('Enter id\n'))
        try:
            return service.data[id]
        except:
            return 'File not found'

class list_getter(i_strategy):
    def do_something(service: Fileservice):
        lst_of_paths = []
        for i in range(int(input('How many files you want to get ? \n'))):
            lst_of_paths.append(service.get_strategy(file_getter))
        
        return lst_of_paths

class file_deleter(i_strategy):
    def do_something(service: Fileservice):
        id = int(input("Enter id you'd like to delete\n"))
        service.data.pop(id)
        service.counter = id
        print(f'Successfully deleted file with id = {id}')
        
class id_changer(i_strategy):
    def do_something(service: Fileservice):
        old_id = int(input('Enter id of file you want to change: '))
        new_id = int(input('Enter new id: '))
        service.data[new_id] = service.data.pop(old_id)
        service.counter = old_id
        print(f'Changed id from {old_id} to {new_id}')
        
class backuper(i_strategy):
    def do_something(service: Fileservice):
        try:
            save_file = open('save_file.txt', 'w', encoding='utf-8')
            save_file.write(str(service.data))
            print('Backup successfull')
        except:
            print('Nothing to save')