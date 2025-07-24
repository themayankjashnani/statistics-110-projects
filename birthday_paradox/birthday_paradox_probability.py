multipl=1

k = int(input("Enter No. of people: "))
for i in range(k):
        #print(i)
        multipl = multipl*(365-i)
        #print(multipl)

p_occ = 1- (multipl/(365**k))
print("Probability of occuring is "+str(100*p_occ))
