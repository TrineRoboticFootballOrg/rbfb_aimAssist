msg = 10

for i in range(8):
    print((msg & (1<<i))>>i)
