def T():
        a=raw_input("F or C:")
        temp=input("user input temperature:")
        if a=='F':
                result=(temp-32)/1.8
                print(result,"C")
        elif a=="C":
                    result=temp*1.8+32
                    print(result,"F")