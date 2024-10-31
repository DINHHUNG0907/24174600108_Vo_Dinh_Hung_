#bai3
num_1 = float(input("Nhap so thu nhat: "))
num_2 = float(input("Nhap so thu hai: "))
num_3 = float(input("Nhap so thu ba: "))
max_num = num_1

if num_2 > max_num:
    max_num = num_2
    
if num_3 > max_num:
    max_num = num_3
    

print("so lon nhat trong 3 so la {max_num}")  