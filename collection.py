import json
#collection_dictionary={1:'sample'}
def add_collection(value):
    with open('collection_json.json') as f:
       collection_dictionary = json.load(f)
    collection_dictionary[int((list(collection_dictionary.keys())[-1]))+1]=value
    with open('collection_json.json', 'w') as f:
       json.dump(collection_dictionary, f)
def get_collection():
    #print(collection_dictionary)
    with open('collection_json.json') as f:
       collection_dictionary = json.load(f)
       print(collection_dictionary)
def get_Collection_By_id(id):
     with open('collection_json.json') as f:
       collection_dictionary = json.load(f)
     return collection_dictionary.get(str(id))

def query_adder(query):
    with open('Query.json') as f:
       query_dictionary = json.load(f)
    query_dictionary[int((list(query_dictionary.keys())[-1]))+1]=query
    with open('Query.json', 'w') as f:
       json.dump(query_dictionary, f)
def get_Query():
    with open('../Query.json') as f:
        query_dictionary = json.load(f)
    print(query_dictionary)


def get_Query_By_id(id):
    with open('Query.json') as f:
        query_dictionary = json.load(f)
    return query_dictionary.get(str(id))