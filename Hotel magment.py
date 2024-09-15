import mysql.connector
def clear():
  for _ in range(10):
     print()
def add_room():
  conn = mysql.connector.connect(host='localhost', database='hotel', user='root', password='#RaJ*&ch@06')
  cursor = conn.cursor()
  clear()
  print('Add New Room - Screen')
  print('-'*120)
  room_no = input('\n Enter Room No :')
  room_type = input('\n Enter Room Type( AC/DELUX/Super Delux/Queen Delight/ Kings Special/Super Rich Special) :')
  room_rent = input('\n Enter Room Rent (INR) :')
  room_bed = input('\n Enter Room Bed Type(Single/Double/Triple) :')
  sql = 'insert into rooms(room_no,room_type,room_rent,room_bed,status) values \
        ('+room_no+',"'+ room_type.upper()+'",'+room_rent+',"'+room_bed.upper()+'","free");'
  cursor.execute(sql)
  print('\n\n\nRoom No ',room_no, ' Sucessfully Added')
  conn.commit()
  conn.close()
  wait = input('\n\n\n Press any key to continue....')
def add_customer():
  conn = mysql.connector.connect(
      host='localhost', database='hotel', user='root', password='#RaJ*&ch@06')
  cursor = conn.cursor()
  clear()
  print('Add New Customer - Screen')
  print('-'*120)
  name = input('\n Enter Customer Name :')
  address = input('\n Enter Customer Address:')
  phone = input('\n Enter Customer Phone NO :')
  email = input('\n Enter Customer Email ID :')
  id_proof = input('\n Enter Customer ID(Aadhar/Passport/DL/VoterID)  :')
  id_proof_no = input('\n Enter Customer ID proof NO :')
  males = input('\n Enter Total Males :')
  females = input('\n Enter Total Females :')
  children = input('\n Enter Total Childeren :')

  sql2 = 'insert into customer(name,address,phone,email,id_proof,id_proof_no,male,females,children) values \
        ("'+name+'","' + address.upper()+'","'+phone+'","'+email.upper()+'","'+id_proof.upper()+'","'+id_proof_no.upper()+'",'+males+','+females+','+children+');'
  sql2 = cursor.execute
  print('\n\n\nCustomer Added success fully ...............')
  conn.commit()
  conn.close()
  wait = input('\n\n\n Press any key to continue....')
def modify_room():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='#RaJ*&ch@06')
    cursor = conn.cursor()
    clear()
    print(' Change Room Information ')
    print('*'*120)
    print('1.   Room Type')
    print('2.   Room Rent')
    print('3.   Room Bed')
    choice = int(input('Enter your choice :'))
    field_name = ''
    if choice == 1:
       field_name = 'room_type'
    if choice == 2:
       field_name = 'room_rent'
    if choice == 3:
       field_name = 'room_bed'
    room_no  = input('Enter room No :')   
    value = input('Enter new value :')
    sql = 'update rooms set ' +field_name +' = '+ value +' where  room_no =' + room_no +';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    wait = input('\n\n\n Record Updated .............Press any key to continue......')
def modify_customer():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='#RaJ*&ch@06')
    cursor = conn.cursor()
    clear()
    print(' Change Customer Information ')
    print('*'*120)
    print('1.   Name')
    print('2.   Address')
    print('3.   Phone No')
    print('4.   Email ID')
    print('5.   ID Proof')
    print('6.   ID Proof No')
    print('7.   Males')
    print('8.   Females')
    print('9.   Childeren')
    choice = int(input('Enter your choice :'))
    field_name = ''
    if choice == 1:
       field_name = 'name'
    if choice == 2:
       field_name = 'address'
    if choice == 3:
       field_name = 'phone'
    if choice == 4:
       field_name = 'email'
    if choice == 5:
       field_name = 'id_proof'
    if choice == 6:
       field_name = 'id_proof_no'
    if choice == 7:
       field_name = 'males'
    if choice == 8:
       field_name = 'females'
    if choice == 9:
       field_name = 'children'
    cust_no = input('Enter Customer No/ID_proof_No. :')
    value = input('Enter new value :')
    sql = 'update customer set ' + field_name + ' = ' + \
        value + ' where   id_proof_no =' + cust_no + ';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    wait = input(
        '\n\n\n Record Updated .............Press any key to continue......')

def room_booking():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='#RaJ*&ch@06')
    cursor = conn.cursor()
    room_id =input('Enter room no to book :')
    cust_id = input('Enter customer ID :')
    date_of_occ = input('Enter date of occupancy (yyyy-mm-dd) :')
    advance = input('Enter advance amount :')
    sql3 = 'update rooms set status = "occupied" where  room_no  ='+room_id +';'
    sql4 = 'insert into booking(room_id,cust_id,doo,advance) values ('+room_id+','+cust_id+',"'+date_of_occ+'",'+advance+');'
   
    sql3 = cursor.execute
    sql4 = cursor.execute
    print('\n\n\nRoom no ', room_id, 'booked for', cust_id)
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_rooms():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='#RaJ*&ch@06')
    cursor = conn.cursor()
    room_no = input('Enter Room No :')
    sql ='select * from rooms where room_no ='+room_no +';'
    cursor.execute(sql)
    record = cursor.fetchone()
    clear()
    print('Room Status')
    print('*'*120)
    print('Room NO :',record[1])
    print('Room Rent :',record[2])
    print('Room Bed :',record[3])
    print('Room Status :',record[4])
    conn.close()
    wait = input('\n\n\nPress any key to continue......')
 
def search_customer():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='#RaJ*&ch@06')
    cursor = conn.cursor()
    
    clear()
    print('Search Customer DataBase')
    print('*'*120)
    print('1.   Customer Name')
    print('2.   Customer Address')
    print('3.   Customer Phone')
    print('4.   Customer Email')
    print('5.   Address Proof')
    print('6.   Address Proof ID')
    choice = int(input('Enter your choice : '))
    field_name =''
    if choice ==1:
      field_name = 'name'
    if choice ==2:
      field_name = 'address'
    if choice ==3:
      field_name = 'phone'
    if choice ==4:
      field_name = 'email'
    if choice ==5:
      field_name = 'id_proof'
    if choice ==6:
      field_name = 'id_proof_no'
    value = input('Enter value that you want to search :')
    if field_name =='id_proof_no':
      sql = 'select * from customer where '+ field_name +' = '+ value + ';'
    else:
      sql = 'select * from customer where ' + field_name + ' like "%' + value + '%";'
    print(sql)
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for {} = {}'.format(field_name,value))
    print('*'*140)
    print('{:10} {:20} {:10} {:15} {:15} {:25}'.format('Name','Address','Phone','Email','ID Used','ID No'))
    for record in records:
      print('{:10} {:20} {:10} {:15} {:10} {:10} '.format(
          record[0], record[1], record[2], record[3], record[4], record[5]))

    conn.close()
    wait = input('\n\n\nPress any key to continue......')

def search_booking():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='#RaJ*&ch@06')
    cursor = conn.cursor()
    cust_no = input('Enter Customer No :')
    sql = 'select r.room_no,c.name,doo,advance from booking b, customer c,rooms r where b.room_id = r.room_no AND b.cust_id = '+cust_no+';'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Booking information for customer ID :{}'.format(cust_no))
    print('{:10} {:20} {:10} {:20}'.format('RoomID', 'Customer Name','Date of Occupancy','Advance'))
    print('*'*140)
    for record in records:
      print('{} {:5} {:5} {:15} '.format(
          record[0], record[1], record[2], record[3]))
    conn.close()
    wait = input('\n\n\nPress any key to continue......')

def search_menu():
    while True:
      clear()
      print(' Search Menu')
      print('*'*120)
      print("\n1.  Room Status")
      print('\n2.  Booking Status')
      print('\n3.  customer Details')
      print('\n4.  Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice==1:
        search_rooms()
      if choice==2:
        search_booking()
      if choice==3:
        search_customer()
      if choice==4:
        break

def main_menu():
    while True:
      clear()
      print(' H O T E L   M A N A G E M E N T   S Y S T E M ')
      print('*'*100)
      print("\n1.   Add New Room")
      print('\n2.   Add Customer')
      print('\n3.   Modify Room Information')
      print('\n4.   Modify Customer Information')
      print('\n5.   Room Booking')
      print('\n6.   Search Database')
      print('\n7.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_room()
      if choice == 2:
        add_customer()
      if choice == 3:
        modify_room()
      if choice == 4:
        modify_customer()
      if choice == 5:
        room_booking()
      if choice == 6:
        search_menu()
      if choice == 7:
        break

if __name__ == "__main__":
  
  main_menu()

