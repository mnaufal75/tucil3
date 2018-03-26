import math

lists = []
encoded = []
decoded = []


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


def mx(message, a, b, p, k, lists):
    found = False
    i = 1
    while (i < k and not found):
        x = message * k + i
        y = 0
        while (y < p and not found):
            if (y * y) % p == ((x * x * x) + (a * x) + b) % p:
                found = True
                lists.append((x, y))
                # print(x, y)
            y += 1
        i += 1


def koblitzEncoding(messages, a, b, p, koblitzBase, lists):
    for message in messages:
        mx(messageToNumber(message), a, b, p, koblitzBase, lists)


def koblitzDecoding(decoded, a, b, p, koblitzBase):
    for i in decoded[1:]:
        # print((i - 1) // koblitzBase)
        print(numberToMessage((i - 1) // koblitzBase))


def encrypt(messages, a, b, p, baseX, baseY, privateKey, k):
    # kB
    lists.append((k * baseX, k * baseY))

    # Pm + kPb
    koblitzEncoding(messages, -1, 188, 751, 20, lists)

    # print(lists[0])
    encoded.append(lists[0])
    for i in range(1, len(lists)):
        # print(lists[i])
        encoded.append((lists[i][0] + k * privateKey * baseX, lists[i][1] + k * privateKey * baseY))
    for i in range(0, len(encoded)):
        print((lists[i][0] - 1) // 20)
    # for a in lists[1:]:
    #     print((a[0], a[1]))
    #     encoded.append((a[0] + k * privateKey * baseX, a[1] + k * privateKey * baseY))
        # print((a[0] + k * baseX) - (lists[0][0] * privateKey) - 1)  # , (a[1] + k * baseY) - (lists[0][1] * privateKey))


def decrypt(messages, a, b, p, baseX, baseY, privateKey, k):
    print(encoded[0])
    decoded.append(encoded[0])
    for a in encoded[1:]:
        # print(a[0] + k * baseX, a[1] + k * baseY)
        # print(numberToMessage(((a[0] - (privateKey * encoded[0][0])) - 1) // 10))
        decoded.append(a[0] - privateKey * encoded[0][0])

    koblitzDecoding(decoded, a, b, p, 20)


# basePointGenerator(-1, 188, 751)
encrypt('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', -1, 188, 751, 750, 376, 3, 2)

decrypt(encoded, -1, 188, 751, 750, 376, 3, 2)
