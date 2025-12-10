f = open('AAAAAAA.txt', 'wt')
for i in range(1,10):
    f.write("a" * i + "\n")
f.close()