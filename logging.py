import zipfile
import re

file_zip = zipfile.ZipFile('access_log.zip', 'r')
file_zip.extractall('./')
file_zip.close()
input_file_name = "access_log.txt"
current_result = "data.txt"

input_file = open(input_file_name, mode='r')
selected_data = open(current_result, mode='w')
my_log_file = input_file.read()

look_for = r"2004:03:0[5-9].*|2004:03:[1-5][0-9].*|2004:0[4-5]:[0-5][0-9].*|2004:06:[0-4][0-9].*|2004:06:5[0-5].*"

result = re.findall(look_for, my_log_file)

for item in result:
    selected_data.write(item + '\n')
selected_data.close()

#############################################
look_for1 = r".png"
result1 = re.findall(look_for1, str(result))

i = 0
for item in result1:
    i += 1
print(f'amount of .png requests: {i}')
#############################################

look_for2 = r".jpeg"
result2 = re.findall(look_for2, str(result))

i = 0
for item in result2:
    i += 1
print(f'amount of .jpeg requests: {i}')
##############################################

look_for3 = r".jpg"
result3 = re.findall(look_for3, str(result))

i = 0
for item in result3:
    i += 1
print(f'amount of .jpeg requests: {i}')
#############################################

look_for4 = r".gif"
result4 = re.findall(look_for4, str(result))

i = 0
for item in result4:
    i += 1
print(f'amount of .jpeg requests: {i}')
