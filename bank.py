import sqlite3
import random
conn=sqlite3.connect("bank.db")
x=conn.cursor()
#x.execute('create table accountdet(acc_no char(50) primary key,name char(50),password char(50),balance int,email char(50))')
def create():
    length=8
    na=input("Username")
    email=input("Mail id")
    a=x.execute("SELECT COUNT(*) FROM accountdet")
    for i in a:
        pass
    b='65555'
    c='00000'+str(i[0]+1)
    acc=b+c[-5:]
    digit=['0','1','2','3','4','5','6','7','8','9']
    lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbol=['@','#','!','$','*']
    all=digit+lower+upper+symbol
    randigi=random.choice(digit)
    ranupp=random.choice(upper)
    ranlow=random.choice(lower)
    ransym=random.choice(symbol)
    pas=randigi+ranupp+ranlow+ransym
    for i in range(length-4):
        pas=pas+random.choice(all)
    db(acc,na,pas,email)
def db(acc,na,pas,email):
    bal=500
    x.execute('insert into accountdet(acc_no,name,password,balance,email) values (?,?,?,?,?)',(acc,na,pas,bal,email))
    conn.commit()
    mail(acc,na,pas,email)
def mail(acc,na,pas,email):
    import smtplib
    y=smtplib.SMTP("smtp.gmail.com",587)
    y.starttls()
    y.login("yourmailid@gmail.com","yourpassword")
    message="Created successfully\n\nUsername:{}\n\nAccount_no:{}\n\nPassword:{}".format(na,acc,pas)
    y.sendmail("yourmailid@gmail.com",email,message
    y.quit()
def tran(b):
    z=int(input("amount to be transferred"))
    ze=(input("account amount to be transferred"))
    zn=b[-2]-z
    zk=x.execute("select * from accountdet where acc_no=?",([ze]))
    for be in zk:
       pass
    if zn>=0:
        x.execute("update accountdet set  balance=? where acc_no=?",(zn,b[0]))
        x.execute("update accountdet set  balance=? where acc_no=?",(z+be[-2],ze))
        conn.commit()
        print("success")
    else:
        print("no balance")
def login():
    una=input("Username:")
    pw=input("Password")
    try:
        verify=x.execute('SELECT * FROM accountdet WHERE name=? and password=?',(una,pw))
        for z in verify:
            print(z)
            pass
        if z:
            print("Success")
            tran(z)
    except:
       print("Incorrect details")

def forgotpw():
    import smtplib
    mail=input("Mail id:")
    check=x.execute('SELECT password FROM accountdet WHERE mailid=?',(mail,))
    for i in check:
        mes=i[0]
    y=smtplib.SMTP("smtp.gmail.com",587)
    y.starttls()
    y.login("yourmailid@gmail.com","yourpassword")
    y.sendmail("yourmailid@gmail.com",mail,mes)
    y.quit()

def main():
    n=input("1.Create/2.Login/3.Forgot password")
    if n=="1":
        create()
    elif n=="2":
        login()
    elif n=="3":
        forgotpw()
    else:
        print("Incorrect option")
    main()

main()
