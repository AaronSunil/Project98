def swapFileData():
    # User Input the file names
    file_a = input("Enter the name of the file to be read")
    file_b = input("Enter the name of the file to be written")

    # Data from the files being saved to string objects
    with open(file_a, 'r') as a:
        data_a = a.read()
    
    with open(file_b, 'r') as b:
        data_b = b.read()

    # Swapping the data from the files
    with open(file_a, 'w') as a:
        a.write(data_b)

    with open(file_b, 'w') as b:
        b.write(data_a)
    
    swapFileData()
