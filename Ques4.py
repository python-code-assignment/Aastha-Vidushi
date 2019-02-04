y=[]
x = list(int(x) for x in raw_input("Enter some numbers with comma separated :").split(","))
for i in x:
    if i % 2 != 0:
       y.append(i*i)
print y
