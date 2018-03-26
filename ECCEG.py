import math


def basePointGenerator(a, b, p):
    for x in range(0, p):
        for y in range(0, p):
            if (y * y) % p == ((x * x * x) + (a * x) + b) % p:
                print(x, y)


def messageToNumber(message):
    if (message in '0123456789'):
        return ord(message) - 48
    elif (message in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        return ord(message) - 54


def numberToMessage(number):
    if (number <= 9):
        return chr(number + 48)
    else:
        return chr(number + 54)


def residueModulo(message, a, b, p, koblitzBase):
    found = False
    i = 1
    while (i < koblitzBase and not found):
        x = message * koblitzBase + i
        y = 0
        while (y < p and not found):
            if (y * y) % p == ((x * x * x) + (a * x) + b) % p:
                found = True
                # lists.append((x, y))
                return (x, y)
            y += 1
        i += 1


def koblitzEncoding(messages, a, b, p, koblitzBase):
    lists = []
    for message in messages:
        lists.append(residueModulo(messageToNumber(message), a, b, p, koblitzBase))
    return lists


def koblitzDecoding(decoded, a, b, p, koblitzBase):
    message = ''
    for i in decoded[1:]:
        message += numberToMessage((i - 1) // koblitzBase)
    return message


def encrypt(messages, a, b, p, baseX, baseY, privateKey, k, koblitzBase):
    encoded = []
    ciphertext = []

    # kB
    encoded.append((k * baseX, k * baseY))

    # Pm + kPb
    encoded.extend(koblitzEncoding(messages, -1, 188, 751, koblitzBase))

    ciphertext.append(encoded[0])
    for i in range(1, len(encoded)):
        ciphertext.append((encoded[i][0] + k * privateKey * baseX, encoded[i][1] + k * privateKey * baseY))

    return ciphertext


def decrypt(ciphertext, a, b, p, baseX, baseY, privateKey, k, koblitzBase):
    decoded = []

    decoded.append(ciphertext[0])
    for a in ciphertext[1:]:
        decoded.append(a[0] - privateKey * ciphertext[0][0])

    plaintext = koblitzDecoding(decoded, a, b, p, koblitzBase)
    return plaintext


# basePointGenerator(-1, 188, 751)
ciphertext = encrypt('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', -1, 188, 751, 750, 376, 3, 2, 20)
plaintext = decrypt(ciphertext, -1, 188, 751, 750, 376, 3, 2, 20)

print(plaintext)
