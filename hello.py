#!usr/bin/python3

#name = input('please enter your name:');
#print('hello',name);

#两个数的乘法运算
#print('两个数的乘法运算')
#a = int(input('请输入所需运算的第一个数字:'))
#b = int(input('请输入所需运算的第二个数字:'))
#print('本次运算的结果是:',a*b)

#a = input('请输入用户名和密码：\n用户名:')
#b = input('密码:')
#if(a == 'wupeng' and b == '123456'):
    #print('欢迎回到地球',a)
#else:
    #print('滚回你的火星去吧！欧巴桑！！')
#以上示例告诉 python认为输进去的都是字符串 对于密码这块要不就在判断中加引号，要不就int转换为整数类型

birth = input('birth:')
if birth >= '18':
    print('birth is',birth)
else:
    print('滚回你的火星去吧！')

# for 循环
#students = ['wupeng1','wupeng2','wupeng3']
#for student in students:
    #print(student)

#在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
#n = 0
#while n < 10:
#    n = n + 1
#    if n % 2 == 0:
#        continue
#    print (n)