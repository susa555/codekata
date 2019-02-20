print('welcome to queue')
l=[]
while True:
    print('please select the operation you want to use\n1.enqueue 2.dequeue3.size of stack 4.emptiness 5.exit')
    a=input()
    a=int(a)
    b=len(l)
    if a==1:
        print('enter the number you want to add')
        element=input()
        l.append(element)
        print(l)
    elif a==2:
        if b==0:
            print('cannot pop element because queue is empty')
        else:
            print('pop the number')
            l.pop(0)
            print(l)
    elif a==3:
        print('the size of queue is')
        print(len(l))
        print(l)
    elif a==4:
        if b==0:
            print('queue is empty')
        else:
            print('queue1 is not empty')
    elif a==5:
        print('You have exited the stack')
        break;
    elif a>=6:
        print('We have only five operations\nPlease choose the above options')

