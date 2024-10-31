#bai2
x = float(input("Nhap hoanh do diem M: "))
y = float(input("Nhap tung do diem M: "))
a = float(input("Nhap hoanh do tam I: "))
b = float(input("Nhap tung do tam I: "))
R = float(input("Nhap ban kinh cua hinh tron: "))

khoang_cach_binh_phuomg = (x - a) ** 2 + (y - b) ** 2
ban_kinh_binh_phuong = R ** 2
if khoang_cach_binh_phuomg <= ban_kinh_binh_phuong:
   print(True)
else: 
   print(False)