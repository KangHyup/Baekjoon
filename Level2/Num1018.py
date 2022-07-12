#체스판 다시칠하기

howBig_y, howBig_x = map(int, input().split())

case_1 = ["WBWBWBWB",
          "BWBWBWBW", 
          "WBWBWBWB",
          "BWBWBWBW", 
          "WBWBWBWB",
          "BWBWBWBW", 
          "WBWBWBWB",
          "BWBWBWBW", ]

case_2 = ["BWBWBWBW", 
          "WBWBWBWB",
          "BWBWBWBW", 
          "WBWBWBWB",
          "BWBWBWBW", 
          "WBWBWBWB",
          "BWBWBWBW", 
          "WBWBWBWB",]

def compareBord(Bord):
    Changed_A = 0
    Changed_B = 0
    for y in range(8):
        for x in range(8):
            if Bord[y][x] != case_2[y][x]: Changed_A+=1

    for y in range(8):
        for x in range(8):
            if Bord[y][x] != case_1[y][x]: Changed_B+=1
    
    if Changed_A < Changed_B: return Changed_A
    else: return Changed_B


def makeBord(y, x):
    Bord = []
    for i in range(8):
        Bord.append(data[y+i][x:x+8])
    return Bord


min = 64
data = []
for i in range(howBig_y):
    data.append(input())


for y in range(howBig_y-7):
    for x in range(howBig_x-7):
        newBord = makeBord(y, x)
        howChanged = compareBord(newBord)
        if min > howChanged:
            min = howChanged
        if min == 0: break

print(min)
