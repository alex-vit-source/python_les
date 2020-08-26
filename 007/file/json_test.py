import json

from read_write import read_file, write_to_file

if __name__== '__main__':
    data= read_file('007/file/data.json')
    print('data is ', data, type(data))
    print()

    obj = json.loads(data)
    print(obj, type(obj))
    print(obj['object']['key'], type(obj))

    print('_______________________________________________\n')
    print('dumping object to text\n')
    obj['new_value']='secret'
    data = json.dumps(obj, sort_keys=True, indent=4)
    print (data, type(data))
    write_to_file('007/file/data.json', data , mode='w')
    print (read_file('007/file/data.json'))

