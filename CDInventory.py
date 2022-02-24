#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Jerry Hiseh, 2022-Feb-24, Modified File
#------------------------------------------#


strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
dicRow = {}


# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        # Open txt file and read the file 
        # Use .strip() and .split() to split each row of string to a list(with 3 elements) 
        # Use .append() to add data into lstTbldisp (for display)
        # THIS IS FOR DISPLAY ONLY!! No changes on inventory data in our 2d-table 'lstTbld')
        lstTbldisp = []        
        print('loading data from txt file')
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id':lstRow[0], 'title':lstRow[1], 'artist':lstRow[2]}
            lstTbldisp.append(dicRow)
        objFile.close()
        
        print('item in the dic')
        for row in lstTbldisp:
            print(row)
            
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        # Use dicRow to save id/title/artist with key:value as dictionaries inner data structure
        # Add dicRows to a 2D-table 'lstTbl'
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}        
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        # See what data is in our 2d-table "lstTbl"
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print()
        
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        # Let user input a CD ID number to decide which entry to delete
        # If user wants to delete CD data with ID==1 for example, remove this row of dictionaries data from 2D-table
        delChoice = int(input('Input ID to delete:'))
        i=-1
        for row in lstTbl:
            i=i+1
            if row['id'] == delChoice:
                lstTbl.remove(lstTbl[i])                      
    
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        # We need the 'values' in dictionaries dat only, add them into strRow
        # Use .write() to wrute data into txtfile
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()

    else:
        print('Please choose either l, a, i, d, s or x!')

