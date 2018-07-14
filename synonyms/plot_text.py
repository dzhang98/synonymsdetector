# create 10% ... 90% files

pg2600 = "novel1.txt"
pg7178 = "novel2.txt"
f2600 = open(pg2600, "r" , encoding = "latin1")
f7178 = open(pg7178, "r" , encoding = "latin1")
text2600 = f2600.read()
text7178 = f7178.read()
l2600 = len(text2600)
l7178 = len(text7178)

for i in range(10,101,10):
    pg2600 = "pg2600_" + str(i) + ".txt"
    pg7178 = "pg7178_" + str(i) + ".txt"
    w2600 = open(pg2600, "w", encoding = "latin1")
    w7178 = open(pg7178, "w", encoding = "latin1")

    
    t2600 = text2600[:l2600*i//100]
    t7178 = text7178[:l7178*i//100]
    
    
    w2600.write(t2600)
    
    w7178.write(t7178)
    
    w2600.close()
    w7178.close()

print("done")
    

    
    
