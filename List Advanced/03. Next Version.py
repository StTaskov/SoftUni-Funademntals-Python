version = input().split(".")
version_like_string = "".join(version)
version_like_number = int(version_like_string) + 1
new_version = ".".join(str(version_like_number))
print(new_version)