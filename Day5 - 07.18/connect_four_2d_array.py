connect_four = []

AG = "AG"
RW = "RW"


row1 = []
row2 = []
row3 = []
row4 = []
row4 = []
row5 = []
row6 = []
row7 = []

row1 = ["  ","  ","  ","  ","  ","  ","  ",]
row2 = ["  ","  ","  ",AG, "  ","  ","  ",]
row3 = ["  ","  ", AG, RW, "  ","  ","  ",]
row4 = ["  ","  ",RW, RW, AG, "  ","  ",]
row5 = ["  ",RW, RW, RW, RW, "  ", AG]
row6 = [RW,AG,RW,AG,AG,RW,RW]
row7 = [AG,RW,AG,RW,AG,AG,AG]

connect_four.append(row1)
connect_four.append(row2)
connect_four.append(row3)
connect_four.append(row4)
connect_four.append(row5)
connect_four.append(row6)
connect_four.append(row7)

print("[")
for row in connect_four:
    print(row)



print("]")
