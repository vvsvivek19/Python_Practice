#SOLUTION 16 - File compression
import gzip
import shutil

file_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\text.txt"
compressed_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\compressed_text.txt.gz"
decompressed_path = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\File_Handling\decompressed_text.txt"

data = b"""In a world of swirling galaxies and dancing stars, a lone adventurer, armed with nothing but wit and a rusty compass, embarked on a journey across uncharted lands. He faced perils untold  treacherous rivers, treacherous mountains, and creatures of myth and legend. Yet, with each step, his resolve grew stronger, fueled by an insatiable thirst for knowledge and a yearning for the unknown. He sought not fortune or fame, but the thrill of discovery, the joy of pushing the boundaries of the known."""

#writing data in binary file
with open(file_path, "wb") as file:
    file.write(data)

#compressing the file
with open(file_path,"rb") as file_in:
    with gzip.open(compressed_path,"wb") as file_out:
        shutil.copyfileobj(file_in,file_out)

print("Compression done successfully")

#decompressing the file
with open(compressed_path,"rb") as file_in:
    with gzip.open(decompressed_path,"wb") as file_out:
        shutil.copyfileobj(file_in,file_out)
print("Decompression done successfully")

