ItemsInCart=0
#2 items will be added to cart

if ItemsInCart !=2:
  #  raise exception("Products  cart count not matching")

#other method

  pass  #if we mentioned pass the raise ecception error will not display

assert(ItemsInCart ==0)

#try ,if we use try block the output will not display error moves to catch block
# Catch, in catch block we can write why the error

try:  #without using try condition error will popuped, if we use try then it will move to catch/exception
    with open(filelog.text,"r")as reader:     #file name mentioned wtong
        reader.read()

#except:  #instead of catch we can use except
   # print("some how i have reached this block beacuse ther eis failure in try block")

except Exception as e:
    print(e)


finally:
    print("cleaning up records")



















