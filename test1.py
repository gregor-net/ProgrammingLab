def fun(arg1, arg2):
    print("Arg {}: {}".format(arg1, arg2))
    
def elleva(arg, n=2):
    """help elleva

    Args:
        arg (number): number type int
        n (int, optional): otptional. Defaults to 2.

    Returns:
        _type_: ellevato alla n
    """
    return arg**n
    

print("Valore {A} e valore {B}".format(B=32, A=5))

stringa = "CIAOOO"

print("Valore {A} e valore {B}".format(A=stringa[2], B=stringa[-2]))

A = 1
B = 2

if( A > B):
    print (A)
    
elif(B > A):
        print(B)
else:
    print("aaa")
    
mylist = [1, 2, 3, 4, 5]
 
for item in mylist:
    print(item)
       
for i, item in enumerate(mylist):
      print("Pos {}: {}".format(i, item))
    
fun("aaa","bbb")

print(elleva(2,4))
print(elleva(2))
help(elleva)

     