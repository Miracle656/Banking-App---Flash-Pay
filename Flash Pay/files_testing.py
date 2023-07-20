import os
import glob
path = "C:/Users/Timothy/Documents/CODES/test"
'''
print(os.listdir(path))
for file_name in os.listdir(path):
    if file_name.lower().endswith(".gif"):
        full_path = os.path.join(path, file_name)
        new_file_name = full_path[:-4] + "_backup.gif"
        os.rename(full_path, new_file_name)


print(glob.glob("*.gif"))
'''

user_slots = []
path = "C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay"
files_and_folders = os.listdir(path)
for folder_name in files_and_folders:
    full_path = os.path.join(path, folder_name)
    if os.path.isdir(full_path):
        user_slots.append(full_path[54:])

print(user_slots)

number = input("Enter Number: ")

for i in user_slots:
    if i[:11] == f"0{number}":
        pass
