class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class PrefixCodeTree:
    def __init__(self):
        self.root = Node(0)
    def insert(self, codeword, symbol):
        node = self.root
        for word in codeword:
            if word == 0:
                if node.left == None:
                    node.left = Node(0)
                node = node.left
            elif word == 1:
                if node.right == None:
                    node.right = Node(0)
                node = node.right
        node.val = symbol
    def decode(self, encodeData, datalen):
        dataAsBit = ''.join(format(byte, '08b') for byte in encodeData)
        node = self.root
        result = ''
        for index in range(0,datalen):
            if dataAsBit[index] == '0':
                node = node.left
            elif dataAsBit[index] == '1':
                node = node.right
            if node.val != 0:
                    result += node.val
                    node = self.root
        return result

