'二維陣列107153015胡經倫'
one, two ,three=11,21,31
number=[[one for one in range (one,15)],
        [two for two in range(two,25)],
        [three for three in range(three,35)]]
print(number[0])
print(number[1])
print(number[2])

'讀取二維陣列'
number=[[11,12,13],[22,24,26],[33,35,37]]
for idx,one in enumerate(number):
    print('第{}列:'.format(idx),end='')
    for two in one:
        print(two,end='')
    print()
else:
    print('讀取完畢')