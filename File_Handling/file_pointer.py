file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\my.data"
with open(file_path,'wb') as file:
    file.write(b"abcdefghij")
with open(file_path,'rb') as file:
    print(file.read(2).decode())
    file.seek(3,2)
    print(file.read(1).decode())
    file.tell()
'''
How seek(-3, 2) Works:
Reference Point: 2 means the pointer starts at the end of the file.
If the file has 10 bytes (abcdefghij), the pointer starts at index 10 (right after the last byte, j).
Offset: -3 means move the pointer backward by 3 bytes.
From index 10, move back:
1st step → 9 (at j).
2nd step → 8 (at i).
3rd step → 7 (at h).
Pointer Position: After moving back 3 bytes, the pointer lands at index 7.

'''