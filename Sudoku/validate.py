digits= '123456789'
rows= 'ABCDEFGHI'
cols= digits
values={'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0', 'H3': '0', 'H7': '0', 'I7': '3', 'I4': '0', 'H5': '0', 'F9': '0', 'G7': '5', 'G6': '9', 'G5': '2', 'E1': '7', 'G3': '2', 'G2': '0', 'G1': '0', 'I1': '0', 'C8': '0', 'I3': '5', 'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0', 'G8': '0', 'A1': '0', 'A3': '3', 'A2': '0', 'A5': '2', 'A4': '0', 'A7': '6', 'A6': '0', 'C3': '1', 'C2': '0', 'C1': '0', 'E6': '0', 'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8', 'I9': '0', 'D8': '0', 'I8': '0', 'E4': '0', 'D9': '0', 'H8': '0', 'F6': '8', 'A9': '0', 'G4': '6', 'A8': '0', 'E7': '0', 'E3': '0', 'F1': '0', 'F2': '0', 'F3': '6', 'F4': '7', 'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0', 'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0', 'H4': '2', 'D3': '8', 'B4': '3', 'B5': '0', 'B6': '5', 'B7': '0', 'E9': '8', 'B1': '9', 'B2': '0', 'B3': '0', 'D6': '2', 'D7': '9', 'D4': '1', 'D5': '0', 'B8': '0', 'B9': '1', 'D1': '0'}
def checkSquare(num,key):
        
        flag = True
        iniRow, iniCol = getIniRowAndIniCol(key)
        limRow = iniRow + 2
        aux = iniCol
        limCol = iniCol + 2
        while iniRow <= limRow and flag:
            iniCol = aux
            while iniCol <= limCol:
                if(values[rows[iniRow]+str(iniCol)] == str(num)):
                    if values[rows[iniRow]+str(iniCol)]=='0':
                        return True
                    flag = False
                    break
                iniCol += 1
            iniRow += 1
        return flag
    
def checkLines(num, key):
        flag = True
        row = key[0]
        col = key[1]
        
        for i in range(1,10):
            if(values[(row+str(i))] == num):
                flag = False
                break
        if(flag):
            for j in range(0,9):
                if(values[rows[j]+col] == num):
                    flag = False
                    break
        return flag
    
def getIniRowAndIniCol(key):
        
        row = key[0]
        col = key[1]

        if(row=='A' or row=='B' or row=='C'): iniRow = 0
        elif(row=='D' or row=='E' or row=='F'): iniRow = 3
        else: iniRow = 6
            
        if(col=='1' or col<='2' or col=='3'): iniCol = 1
        elif(col=='4' or col<='5' or col=='6'): iniCol = 4
        else: iniCol = 7
        return iniRow,iniCol

print checkSquare('0','I8')
print checkLines('0','A2')