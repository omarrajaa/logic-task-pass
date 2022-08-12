
# Q2/Write a program to find all prime numbers up to a given range of numbers?

# solution :
# first the program need input and output

# input
# range should be  from number >> to other
lv = int(input ("Please, Enter the Lowest Range Value: ")) # lv = lower value
uv = int(input ("Please, Enter the Upper Range Value: "))  # uv = upper value

for j in range(lv,uv+1):   # j numbers from lv to uv
    if j > 1:
        for i in range(2,int(pow(j,1/2)+1)):     # i range from 2 to square of j  (use square of j to reduce time of computation)
            if (j%i) == 0:
                break   # if j is not prime :  break
        else:
            # output
            print(j)    # if j is ptime : print