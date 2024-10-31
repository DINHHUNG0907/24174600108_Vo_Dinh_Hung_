#bai4 
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Sắp xếp để dễ kiểm tra
sides = sorted([a, b, c])
a, b, c = sides[0], sides[1], sides[2]

# Kiểm tra điều kiện tam giác
if a + b > c:
    # Kiểm tra loại tam giác
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or b == c:
        print("Đây là tam giác cân.")
    elif a**2 + b**2 == c**2:
        print("Đây là tam giác vuông.")
    elif a == b and a**2 + b**2 == c**2:
        print("Đây là tam giác vuông cân.")
    else:
        print("Đây là tam giác thường.")
else:
    print("Đây không phải là bộ ba cạnh của tam giác.")