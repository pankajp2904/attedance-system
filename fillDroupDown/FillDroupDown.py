import database_handling as dh
class Droupdown:
    list1=[]
    def __init__(self):
        pass
    def fillTeacher(self,Department):
        dict = {0: "--"}
        query={"Dept":Department}
        list=dh.queryExcute(5,query)
        for i in list:
            dict[i["_id"]] = i["name"]
        return dict
    def fillSubject(self,Dept,Sem):
        dict={0:"--"}
        query={"Dept":Dept,"Sem":Sem}
        list=dh.queryExcute(6,query)
        for i in list:
            dict[i["_id"]]=i["Subject_Name"]
        return dict
