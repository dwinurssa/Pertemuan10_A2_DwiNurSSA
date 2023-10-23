#input telah ditentukan
m = 4
n = 5
x = [0]*m
for i in range(m):
    x[i] = [1]*n
print(x)

#input oleh pengguna
m = input("Masukkan jumlah baris: ")
n = input("Masukkan jumlah kolom: ")
x = [0]*m
for i in range(m):
    x[i] = [1]*n
print(x)