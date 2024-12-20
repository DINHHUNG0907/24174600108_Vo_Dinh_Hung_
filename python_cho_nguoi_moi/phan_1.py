    def __init__(self, ma, ten, tuoi, vi_tri, huy_chuong):
        self.ma = ma
        self.ten = ten
        self.tuoi = tuoi
        self.vi_tri = vi_tri
        self.huy_chuong = huy_chuong
        self.thuong = self.tinh_thuong()

    def tinh_thuong(self):
        if self.huy_chuong > 10: return self.huy_chuong * 500000
        elif self.huy_chuong >= 5: return self.huy_chuong * 300000
        elif self.huy_chuong >= 1: return self.huy_chuong * 200000
        return 0

    def __str__(self):
        return f"{self.ma} - {self.ten} - {self.tuoi} - {self.vi_tri} - {self.huy_chuong} huy chuong - Thuong: {self.thuong}"

def nhap_cau_thu():
    try:
        ma = input("Ma cau thu: ")
        ten = input("Ten cau thu: ")
        tuoi = int(input("Tuoi: "))
        vi_tri = input("Vi tri (thu mon/hau ve/tien ve/tien dao): ").lower()
        assert vi_tri in ["thu mon", "hau ve", "tien ve", "tien dao"], "Vi tri khong hop le"
        huy_chuong = int(input("So huy chuong: "))
        assert huy_chuong >= 0, "So huy chuong phai >= 0"
    except (ValueError, AssertionError) as e:
        print(f"Loi: {e}")
        return None
    return CauThu(ma, ten, tuoi, vi_tri, huy_chuong)

def main():
    cau_thus = []
    while True:
        print("\n1. Xem danh sach\n2. Nhap cau thu\n3. Xoa cau thu\n4. Chinh sua\n5. Sap xep\n6. Thoat")
        chuc_nang = input("Chon chuc nang: ")
        
        if chuc_nang == '1':
            for cau_thu in cau_thus:
                print(cau_thu)
        elif chuc_nang == '2':
            cau_thu = nhap_cau_thu()
            if cau_thu: cau_thus.append(cau_thu)
        elif chuc_nang == '3':
            ma_xoa = input("Nhap ma cau thu can xoa: ")
            cau_thus = [ct for ct in cau_thus if ct.ma != ma_xoa]
        elif chuc_nang == '4':
            ma_chinh_sua = input("Nhap ma cau thu can chinh sua: ")
            for ct in cau_thus:
                if ct.ma == ma_chinh_sua:
                    ct.ten = input("Ten moi: ")
                    ct.tuoi = int(input("Tuoi moi: "))
                    ct.vi_tri = input("Vi tri moi: ")
                    ct.huy_chuong = int(input("So huy chuong moi: "))
                    ct.thuong = ct.tinh_thuong()
                    break
        elif chuc_nang == '5':
            cau_thus.sort(key=lambda x: x.huy_chuong)
            for ct in cau_thus:
                print(ct)
        elif chuc_nang == '6':
            break

if __name__ == "_main_":
    main()