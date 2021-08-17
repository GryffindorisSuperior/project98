def swapFileData():
    inputFile1 = input("Enter file name 1: ")
    inputFile2 = input("Enter file name 2: ")

    with open(inputFile1, 'r') as a:
        data_a = a.read()

    with open(inputFile2, 'r') as b:
        data_b = b.read()

    with open(inputFile1, 'w') as a:
        a.write(data_b)

    with open(inputFile2, 'w') as b:
        b.write(data_a)

swapFileData()