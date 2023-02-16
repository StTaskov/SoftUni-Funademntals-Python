file = input().split('\\')

file_name = file[-1]
file_name = file_name.split(".")

print(f"File name: {file_name[0]}")
print(f"File extension: {file_name[1]}")