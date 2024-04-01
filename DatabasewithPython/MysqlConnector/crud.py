import dbconnection
db_conn=dbconnection.connectDB()
#db_conn.autocommit(True)
import json

def addUser():
  try:
    cursor = db_conn.cursor(dictionary=True)
    #print("Add user",db_conn)
    query="""
      INSERT INTO members(FirstName,LastName,Email,Country)VALUES(%s,%s,%s,%s)
    """
    values=("khadar2","basha2","khadar2@gmail.com","UK")
    cursor.execute(query,values)
    db_conn.commit()
    print(cursor.lastrowid)
    user_id=cursor.lastrowid
    cursor.close()
    db_conn.close()
    
    return json.dumps({
      user_id:user_id
    })
    
  except Exception as e:
    db_conn.close()
    return e
    
  
def updateUser():
  cursor = db_conn.cursor(dictionary=True)
  print("Update user")
  try:
    query="""UPDATE members SET FirstName=%s WHERE MemberID=%s"""
    cursor.execute(query,("Sayyad",2))
    db_conn.commit()
    readSelectedUser(2)
    cursor.close()
    db_conn.close()
  except Exception as e:
    return e

def readUser():
  cursor = db_conn.cursor(dictionary=True)
  print("Read user")
  query="""SELECT * FROM members"""
  cursor.execute(query)
  userResult=cursor.fetchall()
  
  for user in userResult:
    print(user['MemberID'])
  
  db_conn.commit()
  #cursor.close()
  #db_conn.close()

def readSelectedUser(userID):
  cursor = db_conn.cursor(dictionary=True)
  print(userID)
  try:
    print("Read user")
    query=f"SELECT * FROM members WHERE MemberID={userID}"
    cursor.execute(query)
    userResult=cursor.fetchone()
    print(userResult)
    db_conn.commit()
  except Exception as e:
    print(e)
      
def readOneUser():
  cursor = db_conn.cursor(dictionary=True)
  try:
    print("Read user")
    query="SELECT * FROM members limit 0,1"
    cursor.execute(query)
    userResult=cursor.fetchone()
    print(userResult)
    db_conn.commit()
  except Exception as e:
    print(e)
  
def deleteUser():
  print("Delete user")


#addUser()
#readUser()
#readOneUser()
#updateUser()