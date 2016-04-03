def rsp():
    userA=raw_input('user A:')
    userB=raw_input('usef B:')
    if userA=='r':
        if userB=='s':
            print "%s" %"userA WIN"
        elif userB=='p':
            print "%s" %"userB WIN"
        else:
            print "%s" %"DRAW"
    elif userA=='s':
        if userB=='r':
            print "%s" %"userB WIN"
        elif userB=='p':
            print "%s" %"userA WIN"
        else:
            print "%s" %"DRAW"
    elif userA=='p':
        if userB=='r':
            print "%s" %"userA WIN"
        elif userB=='s':
            print "%s" %"userB WIN"
        else:
            print "%s" %"DRAW"
rsp()
wn.exitonclick()