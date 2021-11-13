import os
b = 102400
kb = b*100



def read_in_chunks(file_object, chunk_size=kb):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


f = open('E:\\FATEC\\PI\\Files\\K3241.K03200DV.D90805.L00001')
count = 1
for piece in read_in_chunks(f):
    print(piece)
    new = open('E:\\FATEC\\PI\\Files\\frags\\frag'+str(count)+'.txt', 'w')
    new.writelines(piece)
    new.close()
    count += 1
