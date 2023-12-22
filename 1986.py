n = int(input())
hex = input()

byte = bytes.fromhex(hex)
string = byte.decode()
print(string)


# n = int(input())
# hexas = input().split()

# x = ""
# for i in range(n):
# d = int(hexas[i], 16)
# x += chr(d)

# print(x)
