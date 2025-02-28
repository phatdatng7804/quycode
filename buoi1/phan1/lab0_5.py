j=[]

for i in range(2000, 3201):
    if(i % 7 == 0) and (i % 5 != 0):
        j.append(str(i)) #them 1 phan tu vao cuoi danh sach
print(','.join(j)) #ghep cac phan tu thanh 1 chuoi co 1 khoang cach