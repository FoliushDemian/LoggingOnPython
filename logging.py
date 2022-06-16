import zipfile
import re

file_zip = zipfile.ZipFile('access_log.zip', 'r')
file_zip.extractall('./')
file_zip.close()

input_file = open("access_log.txt", mode='r')
my_log_file = input_file.read()

look_for = r"2004:03:0[5-9].*|2004:03:[1-5][0-9].*|2004:0[4-5]:[0-5][0-9].*|2004:06:[0-4][0-9].*|2004:06:5[0-5].*"

result = re.findall(look_for, my_log_file)

look_for1 = r".png"
result1 = re.findall(look_for1, str(result))
print(f'amount of .png requests: {len(result1)}')


look_for2 = r".jpeg"
result2 = re.findall(look_for2, str(result))
print(f'amount of .jpeg requests: {len(result2)}')


look_for3 = r".jpg"
result3 = re.findall(look_for3, str(result))
print(f'amount of .jpg requests: {len(result3)}')


look_for4 = r".gif"
result4 = re.findall(look_for4, str(result))
print(f'amount of .gif requests: {len(result4)}')