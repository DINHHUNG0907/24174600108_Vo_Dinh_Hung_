#bai5
char = input("Nhập một ký tự: ")

# Kiểm tra ký tự có phải là chữ cái không
if len(char) == 1 and char.isalpha():
    # Danh sách các nguyên âm
    vowels = "aeiouAEIOU"
    
    if char in vowels:
        print(f"Ký tự '{char}' là nguyên âm.")
    else:
        print(f"Ký tự '{char}' là phụ âm.")
else:
    print("Vui lòng nhập một ký tự hợp lệ.")