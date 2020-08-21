import database_handling as dh
import  random
import  string
from datetime import date

database=''
collection=''

def insert_UserInfo(data):
     data=data.split('|')
     count = dh.count_record_In_collection(2)
     lettersAndDigits = string.ascii_letters + string.digits
     password=''.join((random.choice(lettersAndDigits) for i in range(6)))
     parameter={"_id":count+1,"Teachet_id":data[0],"name":data[1],"Dept":data[2],"address":data[3],"email":data[4],"mobileno":data[5],"Password":password}
     list=[]
     list.append(parameter)
     id=dh.insert(list,2)
     return id
def login(data):
     loginstatus=dh.loginvalidation(2,data)
     if(loginstatus==None):
          return False
     else:
          return True
def insert_student(data):
     list = []
     count=dh.count_record_In_collection(3)
     for i in data:
          data=i
          count=count+1
          parameter={"_id":count,"Roll_no":data[0],"Name":data[1],"Dept":data[2],"Class":data[3],"Div":data[4]}
          list.append(parameter)
     id=dh.insert(list,3)
     return id
def Search(query,id,conten):
     list2=[]
     list=dh.queryExcute(id,query)
     if(conten=="Presenti"):
          for i in list:
               list1 = []
               list1.append(round(i["_id"])), list1.append(round(i['Roll_no'])), list1.append(i['Name'])
               list2.append(list1)
          print(list2)
     else:
          for i in list:
               list1 = []
               list1.append(round(i["_id"])),list1.append(round(i['Roll_no'])), list1.append(i['Name']), list1.append(i['Dept']), list1.append(i['Class'])
               list2.append(list1)
          print(list2)
     return list2
def inset_Sunject(data):
     list=[]
     count = dh.count_record_In_collection(4)
     parameter={"_id":count+1,"Dept":data[0],"Sem":data[1],"Subject_Name":data[2]}
     list.append(parameter)
     id=dh.insert(list,4)
     return id
def get_Subjct(id,query):
     list2=[]
     list = dh.queryExcute(id, query)
     for i in list:
          list1 = []
          list1.append(i["_id"]),list1.append(i['Dept']), list1.append(i['Sem']), list1.append(i['Subject_Name'])
          list2.append(list1)
     return list2
def insert_Assign_Subject(data):
     list=[]
     count = dh.count_record_In_collection(7)
     parameter={"_id":count+1,"Dept":data[0],"Sem":data[1],"TeacherID":data[2],"SubjectID":data[3]}
     list.append(parameter)
     id = dh.insert(list, 7)
     return id
def get_Assign_Subject():
     list2=[]
     data=dh.exec_big_query('')
     for x in data:
          list1 = []
          list1.append(x["_id"])
          list1.append(x["Dept"])
          list1.append(x["Sem"])
          list1.append(x["teacher_name"]["name"])
          list1.append(x["subject_name"]["Subject_Name"])
          list2.append(list1)
     return list2
def insert_Attendance(data):
     list = []
     count = dh.count_record_In_collection(8)
     parameter = {"_id": count + 1,"Date":date.today().strftime("%d/%m/%Y"), "Dept": data[0],"Class":data[1],"Sem": data[2], "TeacherID": data[3], "SubjectID": data[4],"Present":data[5]}
     list.append(parameter)
     id = dh.insert(list, 8)
     return id
def count(query,collection_id):
     count=dh.count_record_In_collection(query,collection_id)
     return  count;
