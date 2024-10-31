#bai7
a1 = float(input("Nhap a1:" ))
b1 = float(input("Nhap b1:" ))
c1 = float(input("Nhap c1:" ))
a2 = float(input("Nhap a2:" ))
b2 = float(input("Nhap b2:" ))
c2 = float(input("Nhap c2:" ))

D = a1 * b2 - a2 * b1
if D == 0:
    if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
     print("hpt cs vo so nghiem")
    else:
        print("hpt vo nghiem")
else:
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * b2
    
    x = Dx / D
    y = Dy / D
    print(f"Nghiem cua hpt la: x = {x}, y = {y}")