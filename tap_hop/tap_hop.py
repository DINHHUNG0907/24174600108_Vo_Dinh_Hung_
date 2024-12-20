players = []

def nhap_cau_thu():
    try:
        ma_cau_thu = input("Mã cầu thủ: ")
        ten = input("Tên cầu thủ: ")
        tuoi = int(input("Tuổi cầu thủ: "))
        vi_tri = input("Vị trí (thủ môn/hậu vệ/tiền vệ/tiền đạo): ")
        so_huy_chuong = int(input("Số huy chương: "))
        
        assert ma_cau_thu and ten and vi_tri in ['thủ môn', 'hậu vệ', 'tiền vệ', 'tiền đạo']
        assert tuoi > 0 and so_huy_chuong >= 0
        
        thuong = (so_huy_chuong * 500000) if so_huy_chuong > 10 else (so_huy_chuong * 300000 if 5 <= so_huy_chuong < 10 else so_huy_chuong * 200000 if 1 <= so_huy_chuong < 5 else 0)
        
        players.append({'id': ma_cau_thu, 'name': ten, 'age': tuoi, 'position': vi_tri, 'num_medals': so_huy_chuong, 'bonus': thuong})
    except (ValueError, AssertionError):
        print("Dữ liệu nhập vào không hợp lệ!")

def hien_thi_cau_thu():
    if players:
        for player in players:
            print(player)
    else:
        print("Danh sách cầu thủ trống!")

def xoa_cau_thu():
    ma_cau_thu = input("Nhập mã cầu thủ cần xóa: ")
    global players
    players = [p for p in players if p['id'] != ma_cau_thu]

def sua_cau_thu():
    ma_cau_thu = input("Nhập mã cầu thủ cần chỉnh sửa: ")
    for player in players:
        if player['id'] == ma_cau_thu:
            player['name'] = input("Tên mới: ")
            player['age'] = int(input("Tuổi mới: "))
            player['position'] = input("Vị trí mới: ")
            player['num_medals'] = int(input("Số huy chương mới: "))
            player['bonus'] = (player['num_medals'] * 500000 if player['num_medals'] > 10 else player['num_medals'] * 300000 if 5 <= player['num_medals'] < 10 else player['num_medals'] * 200000 if 1 <= player['num_medals'] < 5 else 0)
            break

def sap_xep_cau_thu_theo_huy_chuong():
    players.sort(key=lambda x: x['num_medals'])
    hien_thi_cau_thu()

def menu():
    while True:
        print("\n1. Xem danh sách cầu thủ\n2. Nhập thông tin cầu thủ\n3. Tính thưởng\n4. Xóa cầu thủ\n5. Chỉnh sửa cầu thủ\n6. Sắp xếp cầu thủ\n7. Thoát")
        chon = input("Chọn: ")
        if chon == '1': hien_thi_cau_thu()
        elif chon == '2': nhap_cau_thu()
        elif chon == '3': hien_thi_cau_thu()
        elif chon == '4': xoa_cau_thu()
        elif chon == '5': sua_cau_thu()
        elif chon == '6': sap_xep_cau_thu_theo_huy_chuong()
        elif chon == '7': break
