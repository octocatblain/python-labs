a = str(input("Enter string input: "))
A = ("Spathiphyllum")
B = ("spathiphyllum")

if a == A:
    print("Yes - Spathiphyllum is the best plant ever!")
elif a == B:
    print("No, I want a big Spathiphyllum!")
else: 
    print("Spathiphyllum! Not {}!".format(a))
    print("Spathiphyllum! Not ", a,"!", sep="")
    
    
