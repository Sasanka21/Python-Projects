def linearsearch(data,value):
    found = False
    for i in range(len(data)):
        if data[i] == value:
            found = True
            print(value, ' was found in the list at index ', i)
            break
    if found == False:
        print(value, ' was not found in the list!')
