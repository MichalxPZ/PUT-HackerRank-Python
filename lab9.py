with open("file.txt", 'r') as f :
    read = f.readlines()
    znaki = 0
    słowa = 0
    for i in read:
        znaki += len(i.strip())
        słowa += len(i.split())
    print("Linie: {} \nSłowa: {} \nZnaki: {}".format(len(read), słowa, znaki))