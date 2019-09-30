class Encrypt:
    def encrypt(self,message,password):
        cont = 0
        encrypted = []
        for char in message:
            encrypted.append(chr( ord(char) ^ ord(password[cont % len(password)]) ) )
            cont += 1
        return "".join(encrypted)

    def encryptWMap(self,message,password):
        return "".join(
            list(
                map(
                    lambda x:chr( x ^ ord(password[0]) ),
                    bytearray(message,"utf-8")
                )
            )
        )

e = Encrypt()
msg = "soy buenas"
print(msg)
msg = e.encrypt(msg,"122345")
print(msg)
msg = e.encrypt(msg,"122345")
print(msg)

print("-"*20)

print(msg)
msg = e.encryptWMap(msg,"122345")
print(msg)
msg = e.encryptWMap(msg,"122345")
print(msg)

