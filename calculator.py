while True:
    print("=====SMART CALCULATOR=====")

    A=float(input("Enter your First number="))
    B=float(input("Enter your second number="))
    print("Choose Following Operation")
    print("1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Division")
    print("5-Exit")
    choice=int(input("Enter Your Choice "))
    if choice==1:
        print("Result=",A+B)
    elif choice==2:
        print("Result=",A-B)
    elif choice==3:
        print("Result=",A*B)
    elif choice==4:
            if(B==0):
                 print("Denominator Can,t be zero")
            else:
                 print("Result=",A/B)  
    elif choice==5:
         print("Thank you!!!")
    
    else:
         print("Invalid Choice" )       

    


    

