import gostcrypto

key = bytearray([
        0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77,
        0xfe, 0xdc, 0xba, 0x98, 0x76, 0x54, 0x32, 0x10, 0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
])

class Encoder:
    def __init__(self, key):
        self.key = key

    def encode_gost(self, plain_text, type_enc, filename):
        if type_enc == 'ECB':
            self.cipher_obj = gostcrypto.gostcipher.new('kuznechik',
                                               self.key,
                                               gostcrypto.gostcipher.MODE_ECB)
        else:
            self.cipher_obj = gostcrypto.gostcipher.new('kuznechik',
                                                   self.key,
                                                   gostcrypto.gostcipher.MODE_CBC)
        cipher_text = self.cipher_obj.encrypt(plain_text)
        self.text = plain_text
        with open(filename, 'wb') as f:
            f.write(bytes(cipher_text))

    def decode_gost(self, key, data):
        if key != self.key:
            print('Ошибка: несовпадение ключа')
        else:
            text = self.cipher_obj.decrypt(data)
            if text == self.text:
                print('Данные совпадают')
            else:
                print('Ошибка: контрольные суммы не совпадают')


enc_type = input('Введите желаемый тип (CBC, ECB):')
filename_input = input('Введите название входного файла:')
filename_output = input('Введите название выходного файла:')
encoder = Encoder(key)
with open(filename_input, 'r') as f:
    encoder.encode_gost(filename=filename_output, type_enc=enc_type, plain_text=bytearray(f.read().encode('utf-8')))
