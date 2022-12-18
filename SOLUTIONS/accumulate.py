def accumulate(collection, operation):
  return [operation(x) for x in collection]

#This function takes a collection and an operation as input

squares = accumulate([1, 2, 3, 4, 5], lambda x: x * x)
print(squares)  # [1, 4, 9, 16, 25]

#Note that the lambda function is used to define the operation of squaring the input number.
#This is a simple way to define a short function inline, 
#without the need to define a full function.
