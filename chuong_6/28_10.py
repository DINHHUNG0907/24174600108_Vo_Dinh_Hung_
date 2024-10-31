# 8. Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập. 
# Nếu điểm A thì phân loại là sinh viên xuất sắc, 
# điểm B là sinh viên loại giỏi, 
# điểm C là sinh viên loại khá, 
# điểm D là sinh viên loại trung bình, 
# điểm E là sinh viên loại yếu, 
# điểm F là sinh viên xếp loại kém.

# Hàm xác định loại điểm dựa trên điểm trung bình
def xep_loai_diem(diem_trung_binh):
    if diem_trung_binh >= 9:
        loai = 'A'
    elif 7 <= diem_trung_binh < 9:
        loai = 'B'
    elif 5 <= diem_trung_binh < 7:
        loai = 'C'
    else:
        loai = 'D'
    return loai

# Nhập điểm trung bình
diem_trung_binh = float(input("Nhập điểm trung bình của sinh viên: "))

# Xuất loại điểm
loai_diem = xep_loai_diem(diem_trung_binh)
print(f"Loại điểm của sinh viên là: {loai_diem}")