# slicing indexing [] or slice()
# [start:stop:step]

name = "Bro Code"

name2 = name[0:3]
print(name2)
name3 = name[2:]
print(name3)

funky_name = name[0:8:2]    # name[::2] same
print(funky_name)           # [default 0 : default len-1 : default 1]

split = name.split()
print(split)
first_name = name.split()[0]
last_name = name.split()[1]
print(first_name)
print(last_name)
print(name[::-1])

website = "http://google.com"
print(website[7:13]) # print(website[7:-4]) same

website = "http://youtube.com"
slice = slice(7,-4)
print(website[slice])