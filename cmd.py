import collection as c
def help():
    print("help                     : help")
    print("addCollection value      : add collection")
    print("getCollection                      : get collection")
    print("addQuery query           : add Query")
    print("getQuery                 : get Query ")
def exece():
    cmd=input(">>>")
    cmd=cmd.split(' ')
    if(cmd[0]=="getCollection"):
        c.get_collection()
    if(cmd[0]=="help"):
        help()
    if(cmd[0]=="addCollection"):
        c.add_collection(cmd[1])
    if(cmd[0]=="addQuery"):
        c.query_adder(cmd[1])
    if(cmd[0]=="getQuery"):
        c.get_Query()
help()
a=1
while a==1:
    exece()
