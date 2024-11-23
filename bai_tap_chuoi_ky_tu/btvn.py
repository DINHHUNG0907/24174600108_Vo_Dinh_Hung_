# Bài 1: Nhập vào chuỗi ký tự và đếm số từ trong chuỗi
chuoi_nhap_vao = input("Nhập vào chuỗi ký tự: ")
so_tu = len(chuoi_nhap_vao.split())
print(f"Số từ trong chuỗi là {so_tu}")






# Bài 2: Nhập vào chuỗi ký tự và loại bỏ tất cả các dấu cách thừa
chuoi_nhap_vao = input("Nhập vào chuỗi ký tự: ")
chuoi_sau_xoa = chuoi_nhap_vao.strip()
print(f"Chuỗi sau khi loại bỏ dấu cách thừa: '{chuoi_sau_xoa}'")








# Bài 3: Nhập vào họ tên đầy đủ và trả về họ và tên riêng
chuoi_nhap_vao = input("Nhập vào họ tên đầy đủ: ")
ten_parts = chuoi_nhap_vao.split()
ho = ten_parts[0]
ten = ten_parts[-1]
print(f"Ho: {ho}, Ten: {ten}")









# Bài 4: Đếm số ký tự là chữ, số và ký tự đặc biệt trong chuỗi
chuoi_nhap_vao = input("Nhập vào chuỗi ký tự: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0

for chu in chuoi_nhap_vao:
    if chu.isalpha():
        dem_chu += 1
    elif chu.isdigit():
        dem_so += 1
    else:
        dem_ky_tu_dac_biet += 1

print(f"Số chữ cái: {dem_chu}, Số số: {dem_so}, Số ký tự đặc biệt: {dem_ky_tu_dac_biet}")










# Bài 5: Đếm số chữ cái viết hoa và viết thường trong chuỗi
chuoi_nhap_vao = input("Nhập vào chuỗi ký tự: ")
dem_hoa = 0
dem_thuong = 0

for chu in chuoi_nhap_vao:
    if chu.isupper():
        dem_hoa += 1
    elif chu.islower():
        dem_thuong += 1

print(f"Số chữ cái viết hoa: {dem_hoa}, Số chữ cái viết thường: {dem_thuong}")











# Bài 6: Kiểm tra chuỗi có phải là số âm không
chuoi_nhap_vao = input("Nhập vào chuỗi: ")

if chuoi_nhap_vao.startswith('-') and chuoi_nhap_vao[1:].isdigit():
    print("Chuỗi là số âm.")
else:
    print("Chuỗi không phải là số âm.")













    # Bài 7: Kiểm tra chuỗi có phải là số thập phân không
chuoi_nhap_vao = input("Nhập vào chuỗi: ")

try:
    float(chuoi_nhap_vao)
    if '.' in chuoi_nhap_vao:
        print("Chuỗi là số thập phân.")
    else:
        print("Chuỗi không phải số thập phân.")
except ValueError:
    print("Chuỗi không phải số thập phân.")














# Bài 8: Kiểm tra chuỗi con có nằm trong chuỗi cha không
chuoi_cha = input("Nhập vào chuỗi cha: ")
chuoi_con = input("Nhập vào chuỗi con: ")

if chuoi_con in chuoi_cha:
    print(f"Chuỗi con '{chuoi_con}' có trong chuỗi cha '{chuoi_cha}'.")
else:
    print(f"Chuỗi con '{chuoi_con}' không có trong chuỗi cha '{chuoi_cha}'.")















# Bài 9: Kiểm tra chuỗi nhị phân và chuyển đổi sang số thập phân
chuoi_nhap_vao = input("Nhập vào chuỗi nhị phân: ")

if all(bit in '01' for bit in chuoi_nhap_vao):
    decimal_value = int(chuoi_nhap_vao, 2)
    print(f"{chuoi_nhap_vao} là số nhị phân, chuyển sang thập phân: {decimal_value}")
else:
    print("Chuỗi không phải là số nhị phân.")











# Bài 10: Dồn tất cả số sang bên trái
chuoi_nhap_vao = input("Nhập vào chuỗi: ")

so = ''.join([char for char in chuoi_nhap_vao if char.isdigit()])
ky_tu_khac = ''.join([char for char in chuoi_nhap_vao if not char.isdigit()])
chuoi_ket_qua = so + ky_tu_khac
print(f"Chuỗi sau khi dồn số sang bên trái: {chuoi_ket_qua}")    