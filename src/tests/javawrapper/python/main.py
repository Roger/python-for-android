import time
from java import JavaClass, JavaMethod, JavaStaticMethod, JavaField, JavaStaticField

class Test(JavaClass):
    __javaclass__ = 'org/javawrapper/Test'

    methodZ = JavaMethod('()Z')
    methodB = JavaMethod('()B')
    methodC = JavaMethod('()C')
    methodS = JavaMethod('()S')
    methodI = JavaMethod('()I')
    methodJ = JavaMethod('()J')
    methodF = JavaMethod('()F')
    methodD = JavaMethod('()D')
    methodString = JavaMethod('()Ljava/lang/String;')

    methodStaticZ = JavaStaticMethod('()Z')
    methodStaticB = JavaStaticMethod('()B')
    methodStaticC = JavaStaticMethod('()C')
    methodStaticS = JavaStaticMethod('()S')
    methodStaticI = JavaStaticMethod('()I')
    methodStaticJ = JavaStaticMethod('()J')
    methodStaticF = JavaStaticMethod('()F')
    methodStaticD = JavaStaticMethod('()D')
    methodStaticString = JavaStaticMethod('()Ljava/lang/String;')

    fieldZ = JavaField('Z')
    fieldB = JavaField('B')
    fieldC = JavaField('C')
    fieldS = JavaField('S')
    fieldI = JavaField('I')
    fieldJ = JavaField('J')
    fieldF = JavaField('F')
    fieldD = JavaField('D')
    fieldString = JavaField('Ljava/lang/String;')

    fieldStaticZ = JavaStaticField('Z')
    fieldStaticB = JavaStaticField('B')
    fieldStaticC = JavaStaticField('C')
    fieldStaticS = JavaStaticField('S')
    fieldStaticI = JavaStaticField('I')
    fieldStaticJ = JavaStaticField('J')
    fieldStaticF = JavaStaticField('F')
    fieldStaticD = JavaStaticField('D')
    fieldStaticString = JavaStaticField('Ljava/lang/String;')

def do(msg, value, want):
    print 'Testing', msg, ':', (value, want), '-->', (value == want)


print '--------------- TESTS ----------------'
test = Test()

print '-- test static methods'
do('method bool', test.methodStaticZ(), True)
do('method byte', test.methodStaticB(), 127)
do('method char', test.methodStaticC(), 'k')
do('method short', test.methodStaticS(), 32767)
do('method int', test.methodStaticI(), 2147483467)
do('method long', test.methodStaticJ(), 2147483467)
do('method float', test.methodStaticF(), 1.23456789)
do('method double', test.methodStaticD(), 1.23456789)
do('method String', test.methodStaticString(), 'helloworld')

print '-- test static field'
do('field bool', test.fieldStaticZ, True)
do('field byte', test.fieldStaticB, 127)
do('field char', test.fieldStaticC, 'k')
do('field short', test.fieldStaticS, 32767)
do('field int', test.fieldStaticI, 2147483467)
do('field long', test.fieldStaticJ, 2147483467)
do('field float', test.fieldStaticF, 1.23456789)
do('field double', test.fieldStaticD, 1.23456789)
do('field String', test.fieldStaticString, 'helloworld')

print '-- test methods'
do('method bool', test.methodZ(), True)
do('method byte', test.methodB(), 127)
do('method char', test.methodC(), 'k')
do('method short', test.methodS(), 32767)
do('method int', test.methodI(), 2147483467)
do('method long', test.methodJ(), 2147483467)
do('method float', test.methodF(), 1.23456789)
do('method double', test.methodD(), 1.23456789)
do('method String', test.methodString(), 'helloworld')

print '-- test field'
do('field bool', test.fieldZ, True)
do('field byte', test.fieldB, 127)
do('field char', test.fieldC, 'k')
do('field short', test.fieldS, 32767)
do('field int', test.fieldI, 2147483467)
do('field long', test.fieldJ, 2147483467)
do('field float', test.fieldF, 1.23456789)
do('field double', test.fieldD, 1.23456789)
do('field String', test.fieldString, 'helloworld')

print '--------------- ENDTESTS ----------------'