from collections import deque
import random

class FancyDES():

    def __init__(self, message, key):
        self.message = message
        self.key = key

    def message_to_block(self, message = ''):
        self.block_left = [
            ['0xFF','0xF5', '0xF4', '0xF2'],
            ['0x5F','0x35', '0x24', '0x12'],
            ['0xFF','0xF5', '0xF4', '0x42'],
            ['0x6F','0x55', '0x24', '0x32'],
            ]
        self.block_right = [
            ['0xFF','0xF5', '0xF4', '0xF2'],
            ['0x5F','0x35', '0x24', '0x12'],
            ['0xFF','0xF5', '0xF4', '0x42'],
            ['0x6F','0x55', '0x24', '0x32'],
        ]

    def transpose(self, message = None):
        output = [[message[3-i][j] for i in range(4)] for j in range(4)]
        return output

    def xor(self, message = None, key = None):
        output = []
        for i in range(4):
            new = []
            for j in range(4):
                temp = int(message[i][j], 16) ^ int(key[i][j], 16)
                new.append('0x{:02X}'.format(temp))
            output.append(new)
        return output

    def xor_strings(self, xs, ys):
        return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

    def shift(self, message = None, key = None):
        output = []
        for i in range(4):
            sum = 0
            item = deque(message[i])
            for num in key[i]:
                sum += int(num,16)
            print(sum%4)
            if (i % 2 == 0):
                item.rotate((sum % 4) * -1)
            else:
                item.rotate(sum%4)
            output.append(list(item))
        return output

    def generate_chiper(self):
        sum = 0
        for i in self.key:
            sum += ord(i)
        print(sum)
        random.seed(sum)
        round = random.randint(1,25)
        print(round)
        if round < 7:
            round = 7
        return round
if __name__ == '__main__':
    key_internal = [
            ['0xFF','0xF5', '0xF9', '0xF2'],
            ['0x5F','0x35', '0x25', '0x12'],
            ['0xFF','0xF5', '0x64', '0x42'],
            ['0x6F','0x55', '0x53', '0x32'],
        ]
    block_right = [
        ['0xFF','0xF5', '0xF4', '0xF2'],
        ['0x5F','0x35', '0x24', '0x12'],
        ['0xFF','0xF5', '0xF4', '0x42'],
        ['0x6F','0x55', '0x24', '0x32'],
    ]
    fancyDES = FancyDES('HELLO','HELLO WORLD! HAHAHHA')
    #print(fancyDES.shift(message=block_right,key=key_internal)) 
    #print(fancyDES.transpose(block_right))
    #print(fancyDES.xor(block_right, key_internal))
    print(fancyDES.generate_chiper())