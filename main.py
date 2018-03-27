import time
import codecs
import ECCEG

print("Masukkan metode enkripsi yang akan dipakai: ")
print("1. RSA")
print("2. ECC El Gamal")
menu = input()

if (int(menu) == 1):
    pass
elif (int(menu) == 2):
    pilihan = input("Pilih enc atau dec: ")
    if (pilihan == 'enc'):
        a, b, p = map(int, input("Masukkan nilai a, b, dan p: ").split())
        # ECCEG.basePointGenerator(a, b, p)

        baseX, baseY = map(int, input("Masukkan titik basis (X dan Y): ").split())
        koblitzBase = int(input("Masukkan nilai k untuk encoding pesan ke dalam kurva: "))
        privateKey = int(input("Masukkan private key: "))
        k = int(input("Masukkan bilangan acak k untuk enkripsi: "))

        masukan = input("Masukan dari file atau tidak? ")
        messages = ''
        if (masukan == 'Y'):
            inputFile = input("Masukkan nama file plaintext: ")
            with open(inputFile) as inf:
                for line in inf:
                    messages += line
            print(messages)
        else:
            messages = input("Masukkan pesan yang akan dikirim: ")

        start = time.time()
        ciphertext = ECCEG.encrypt(messages, a, b, p, baseX, baseY, privateKey, k, koblitzBase)
        end = time.time()

        string = ''
        for line in ciphertext:
                string += str(line[0]) + ' ' + str(line[1]) + '\n'
        print(codecs.encode(string.encode(), 'hex'))
        print("Enkripsi dilakukan dalam waktu", end - start, "detik")

        inputFile = input("Masukkan nama file penyimpanan: ")
        with open(inputFile, 'w') as inf:
            for line in ciphertext:
                inf.write(str(line[0]) + ' ' + str(line[1]) + '\n')

    elif (pilihan == 'dec'):
        ciphertext = []
        inputFile = input("Masukkan nama file ciphertext: ")
        with open(inputFile) as inf:
            for line in inf:
                x, y = map(int, line.split())
                ciphertext.append((x, y))

        a, b, p = map(int, input("Masukkan nilai a, b, dan p: ").split())
        baseX, baseY = map(int, input("Masukkan titik basis (X dan Y): ").split())
        koblitzBase = int(input("Masukkan nilai k untuk encoding pesan ke dalam kurva: "))
        privateKey = int(input("Masukkan private key: "))
        k = int(input("Masukkan bilangan acak k untuk enkripsi: "))

        start = time.time()
        plaintext = ECCEG.decrypt(ciphertext, a, b, p, baseX, baseY, privateKey, k, koblitzBase)
        end = time.time()
        print("Dekripsi dilakukan dalam waktu", end - start, "detik")
        print(plaintext)
