
class Cho(object):
    def __init__(self, param1):
        self.x = 'hello'
        self.param1 = param1
        print('this is __init__ x:{}  param1:{}'.format(self.x, self.param1))

    # def __str__(self):
    #     return
    #     # return 'this is __str__ x:{}  param1:{}'.format(self.x, self.param1)

a = Cho(1)
print("--------------")
a = Cho(1)
# print('%s'%a)
print('%s'%a)
