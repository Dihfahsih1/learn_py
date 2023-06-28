ls = ['difas','dickson','winnie','denis']

for i in range(len(ls)):
    if ls[i] == 'winnie':
        print(ls[i] + " is first born ")

    elif ls[i] == 'difas':
        print(ls[i] + " is the second born ")

    elif ls[i] == 'dickson':
        print(ls[i] + " is the third born ")
    else:
        print(ls[i] + " is the last born ")