#Exceptional Handing

a=5
b=0

try:
    print("resource open")
    print(a/b)

#except Exception:
    #print("Hey, you cannot divide a number by zero")
    
#OR
    
except Exception as e:
    print("Hey, you cannot divide a number by zero-", e)
#print("bye")

finally:
    print("resource closed")

