# learned that the correct ordering of base classes and mixins when declaring a new class is right to left.
# right starts with base class and then moving left the mixins are added in.

# also you can 
class BaseClass:
    myVar = 'Hello'
    def test(self):
        print ("BaseClass")
    
    def baseTest(self):
        print ("the basetest function")

class Mixin1(object):
    def test(self):
        print ("Mixin1")

class Mixin2(object):
    def test(self):
        print ("Mixin2")
        print (self.myVar)

class MyClass(Mixin2, Mixin1, BaseClass):
    pass

class MyClass2(Mixin1, Mixin2, BaseClass):
    pass

class MyClass3(BaseClass, Mixin1, Mixin2):
    pass

class MyClass4(BaseClass):
    pass

if __name__=='__main__':
    obj1 = MyClass()
    obj2 = MyClass2()
    obj3 = MyClass3()
    obj4 = MyClass4()

    print()
    print('1) this uses the test function from Mixin2')
    obj1.test()
    obj1.baseTest()
    print()

    print('2) this uses the test function from Mixin1')
    obj2.test()
    obj2.baseTest()
    print()

    print('3) this uses the test frunction from BaseClass')
    obj3.test()
    obj3.baseTest()
    print()
    print('4) this uses the test function from Baseclass')
    obj4.test()
    obj4.baseTest()
