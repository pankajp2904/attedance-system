import connection_mangodb as dbconnection
import collection as c
import json

database=''
collection=''
list=[]
if(dbconnection.connection()):
    database=dbconnection.connection()
    #collection=database[]

def insert(list,Coll_id):
    collection=database[str(c.get_Collection_By_id(Coll_id))]
    x=collection.insert_many(list)
    return x.inserted_ids
def loginvalidation(id,data):
    data=data.split('|')
    collection = database[c.get_Collection_By_id(id)]
    result=collection.find({"Teachet_id":data[0],"Password":data[1]})
    for x in result:
       print(x)
       return x
def count_record_In_collection(query,Coll_id):
    collection = database[str(c.get_Collection_By_id(Coll_id))]
    result=collection.find(query).count()
    return result
def queryExcute(Coll_id,query):
    list.clear()
    collection = database[str(c.get_Collection_By_id(Coll_id))]
    result=collection.find(query)
    for x in result:
        list.append(x)
    print(list)
    return list
def exec_big_query(query):
    list.clear()
    query = database["Assign_Subject"].aggregate([{"$lookup":{"localField":"TeacherID","from":"TeacherList","foreignField": "_id", "as": "teacher_name"}},{ "$unwind": "$teacher_name" },{"$lookup":{ "localField":"SubjectID", "from":"Subject_List", "foreignField": "_id", "as": "subject_name"}}, { "$unwind": "$subject_name" }, { "$project": { "_id":1, "Dept":1,"Sem":1, "teacher_name.name":1, "subject_name.Subject_Name":1} } ]);
    result=query
    for x in result:
        list.append(x)
    return list
