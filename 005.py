class Bucket:
    def __init__(self, V):
        self.V = V
        print ('Вместительность задана')
class Packet(Bucket):
    pass
VBuck = Bucket(input('Введите вместимость корзины'))
VPack = Packet(input('Введите вместимость пакета'))