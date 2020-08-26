def read_file(filename):
    print ('Читаем с файла')
    with open(filename) as f:
        return f.read()



def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        f.write(content)



if __name__=='__main__':
    content='\n OOOOOHHHHH'
    write_to_file('007/file/test.txt', content, mode='a')
    print (read_file('007/file/test.txt'))