import pymysql
def db_new(name,ship_class,energy,power,resourceA,resourceB):
    ship_name=name
    ship_class=ship_class
    ship_energy=energy
    ship_power=power
    ship_resourceA=resourceA
    ship_resourceB=resourceB
    db=pymysql.connect("returndb.cusebofqs8mf.ap-southeast-2.rds.amazonaws.com","Kaihu","Ad20010913","returnDB",autocommit=True)
    cursor=db.cursor()
    sql="INSERT INTO RETURN_SHIP_RECORD(SHIP_NAME,SHIP_CLASS,SHIP_ENERGY,SHIP_POWER,SHIP_RESOURCEA,SHIP_RESOURCEB)VALUES(%s,%s,%s,%s,%s,%s)"
    param=(ship_name,ship_class,ship_energy,ship_power,ship_resourceA,ship_resourceB)
        # 执行sql语句
        # try:
    cursor.execute(sql,param)
        # 提交到数据库执行
    #except:
        # 如果发生错误则回滚
        #db.rollback()
    db.close()
def db_update(name,ship_class,energy,power,resourceA,resourceB):
    ship_name=name
    ship_class=ship_class
    ship_energy=energy
    ship_power=power
    ship_resourceA=resourceA
    ship_resourceB=resourceB
    db=pymysql.connect("returndb.cusebofqs8mf.ap-southeast-2.rds.amazonaws.com","Kaihu","Ad20010913","returnDB",autocommit=True)
    cursor=db.cursor()
    sql="UPDATE RETURN_SHIP_RECORD SET SHIP_ENERGY=%s,SHIP_POWER=%s,SHIP_RESOURCEA=%s,SHIP_RESOURCEB=%s WHERE SHIP_NAME=%s"
    param=(ship_energy,ship_power,ship_resourceA,ship_resourceB,ship_name)
        # 执行sql语句
        # try:
    cursor.execute(sql,param)
        # 提交到数据库执行
    #except:
        # 如果发生错误则回滚
        #db.rollback()
    db.close()
    



