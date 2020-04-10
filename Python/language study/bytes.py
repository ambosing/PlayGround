print(bytes(10))
print(bytes([10, 20, 30, 40, 50]))
print(b'hello')

x = bytearray(b'hello')
x[0] = ord('a')
print(x)

print('hello'.encode())
print("안녕".encode('euc-kr'))
print("안녕".encode('utf-8'))

print(b'hello'.decode())
x = '안녕'.encode('euc-kr')
print(x.decode('euc-kr'))