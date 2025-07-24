import matplotlib.pyplot as plt

x=[]
y=[]
p_occ=0
for j in range(366):
        multipl=1
        x.append(j)
        for i in range(j+1):
                #print(i)
                multipl = multipl*(365-i)
                #print(multipl)
                print(i)
                print(j)
                
                if int(i)==int(j): 
                        if i == 0 :
                                p_occ = 0   
                        else:
                                p_occ = 1- (multipl/(365**(j+1))) 
                        y.append(p_occ*100)

plt.plot(x,y)
plt.xlabel('No. of people')
plt.ylabel("Probability %")
plt.title("Birthday Paradox Graph")
plt.show()