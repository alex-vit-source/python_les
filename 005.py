class Bucket:
    some=()
    def __init__(self, V):
        self.V = V
        print ('Вместительность задана')
    def add(self, some):
        self.some=self.some+some
        print ('Добавлено')
        
class Packet(Bucket):
    pass
VBuck = Bucket(input('Введите вместимость корзины'))
VPack = Packet(input('Введите вместимость пакета'))
VBuck.add(input('Добавьте что-то в корзину'))
VPack.add(input('Добавьте что-то в пакет'))
print ('Сейчас в корзине', VBuck.some)
print ('Сейчас в пакете', VPack.some)

