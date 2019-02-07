def removeNone(dictionary):
    for k, v in dictionary.items():
        if isinstance(v, dict):
            removeNone(v)
        elif (v==None):
            dictionary.pop(k)

    return dictionary


Dict = {
        'Dict1': {'name': 'Ali', 'age': 19,'mob':123456},
        'Dict2': {'name': 'Bob', 'age': 22,'mob':123789},
        'Dict3':{'name': 'Cam', 'age': 41,'mob':None},
        'Dict4':{'name': 'Dan', 'age': 44,'mob':None},
        'Dict5':{'name': 'Eak', 'age': 15,'mob':456987},
        'Dict0':[]
        }
if __name__=='__main__':
    res=removeNone(Dict)
    print (res)
