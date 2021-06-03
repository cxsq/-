#utf-8
file= open('3.txt', encoding='utf-8')
lst = file.readlines()
for item in lst:
    print(item, end = '')
file.close()
