init = 1
end = 100

for i in range(init,end+1):
    
    if i%3==0:
        print("fizz",end="")
        
    if i%5==0:
        print("buzz",end="")
    
    if i%3 and i%5:
        print(i,end="")
        
    print("")
