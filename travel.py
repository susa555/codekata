print("welcome to fun travels")
place=["tambaram","adayar","ambathur"]
dist=[35,30,50]
print("where you want to go?\n1.tambaram 2.adayar 3.ambathur")
choice=int(input())
if  choice==1:
    kms=dist[0]
elif choice==2:
    kms=dist[1]
elif choice==3:
    kms=dist[2]
print("what type of car you want?\n1.mini 2.nano 3.micro")
mini=5
nano=7
micro=9
car=int(input())
if car==1:
   price =kms*mini
elif car==2:
   price=kms*nano
elif car==3:
    price=kms*micro
print('total amount is',price)
