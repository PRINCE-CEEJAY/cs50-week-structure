file_types = {
    ".gif" : "image/gif",
    ".jpg" : "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
    "default" : "application/octet-stream"
    }

file_name = input("provide the filename ").strip().lower()

three_char_extension = file_name[-4:]
four_char_extension =  file_name[-5:]

if three_char_extension in file_types:
    print(file_types[three_char_extension])

elif four_char_extension in file_types:
    print(file_types[four_char_extension])

else:
    print(file_types["default"])

