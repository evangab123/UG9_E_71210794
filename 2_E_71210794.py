nama = input("Nama : ")
ttl = input("Tempat Tanggal Lahir : ")
x= len(nama)
if x<17:
    namadibalik= ', '.join(reversed(nama.split()))
    print("Haloo!", namadibalik)
else:
    namaterakhir= ''.join(nama.split()[-1::1])
    nama2= ' '.join(nama.split()[0:2:])
    print("Haloo!", namaterakhir + ", " + nama2)
    

tempat= ' '.join(ttl.split()[0:1:])
tanggal=' '.join(ttl.split()[1:4:])

print("Anda lahir di" + " "+ tempat + " " + "pada tanggal"+ " " + tanggal)

    