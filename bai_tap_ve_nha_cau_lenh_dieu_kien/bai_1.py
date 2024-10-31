#bai1
nam = float(input("Nhập năm:"))
if nam > 0:
   if (nam % 4 == 0 and nam % 100 != 0 ):
      print(f"nam do la nam nhuan" )
   elif (nam % 4 == 0 and nam % 400 == 0 ):
      print(f"nam do la nam nhuan:")
   elif (nam % 4 == 0 and nam % 100 == 0):
      print("nam do ko phai la nam nhuan: ")
else:
    print(f"ko ton tai")
print("ket thuc")