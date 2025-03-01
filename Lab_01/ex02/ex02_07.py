print("Nhập các dòng văn bản(Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("Dòng văn bản đã nhập sau khi chuyên thành chữ in hoa:")
for line in lines:
    print(line.upper())