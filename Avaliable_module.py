import pymysql
from module_dic import module_dictionary
def module_list(ship_name):
    db=pymysql.connect("returndb.cusebofqs8mf.ap-southeast-2.rds.amazonaws.com","Kaihu","Ad20010913","returnDB")
    cursor=db.cursor(pymysql.cursors.DictCursor)
    sql="SELECT SHIP_CLASS,SHIP_ENERGY,RESOURCE_A_MINER,GENERATOR,REFLECT_SHEILD FROM RETURN_SHIP_RECORD WHERE SHIP_NAME=%s"
    param=ship_name
    cursor.execute(sql,param)
    output=[]
    # cursor.fetchall() can only be call once per query
    i=0
    for key,value in cursor.fetchall()[0].items():
        if value == 'X':
            i+=1
            key=str(i)+"."+key
            output.append(key)
    db.close()
    print("Avalible Module are: ",output)
    return output
    
    
# module_list("test")

def build_module(selection,ship_name):
    db=pymysql.connect("returndb.cusebofqs8mf.ap-southeast-2.rds.amazonaws.com","Kaihu","Ad20010913","returnDB",autocommit=True)
    cursor=db.cursor(pymysql.cursors.DictCursor)

    sql="UPDATE RETURN_SHIP_RECORD SET {}='O' WHERE SHIP_NAME=%s".format(selection)
    param=(ship_name)
    cursor.execute(sql,param)
    db.close()
    print("{} Built".format(selection))
    
    
    
build_module("REFLECT_SHEILD","test")