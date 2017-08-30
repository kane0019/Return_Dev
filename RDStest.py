import pymysql
from module_dic import module_dictionary
def db_test(name,ship_class,energy,power,resourceA,resourceB):
    ship_name=name
    ship_class=ship_class
    ship_energy=energy
    ship_power=power
    ship_resourceA=resourceA
    ship_resourceB=resourceB
    db=pymysql.connect("returndb.cusebofqs8mf.ap-southeast-2.rds.amazonaws.com","Kaihu","Ad20010913","returnDB")
    cursor=db.cursor(pymysql.cursors.DictCursor)
    sql="SELECT SHIP_CLASS,SHIP_ENERGY,RESOURCE_A_MINER,GENERATOR,REFLECT_SHEILD FROM RETURN_SHIP_RECORD WHERE SHIP_NAME=%s"
    para=ship_name
    #sql="""INSERT INTO RETURN_SHIP_RECORD(
    #    SHIP_NAME,SHIP_CLASS,SHIP_ENERGY,SHIP_POWER,SHIP_RESOURCEA,SHIP_RESOURCEB)
    #    VALUES(ship_name,ship_class,ship_energy,ship_power,ship_resourceA,ship_resourceB)
    #   """
    cursor.execute(sql,para)
    output=[]
  #  cursor.fetchall() can only be call once per query
    for key,value in cursor.fetchall()[0].items():
        if value == None:
            output.append(key)
    db.close()
    return output
module_list=db_test("test","testclass",10,0,100,100)
for item in module_list:
    print(module_dictionary(item))
