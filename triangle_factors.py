###FIX ME!!!###
counter = 1
divisors = 0
while divisors < 500:
  divisors = 0
  triNumber = sum(range(1, counter + 1))
  bound = triNumber // 2
  #print(bound)
  for divisor in range(1, bound + 1 if(bound > 0) else 2):
    #print("help")
    if triNumber % divisor == 0: 
      divisors += 1
      #print(triNumber)
      counter += 1
      #Here
      #One of these comments is a lie.
  divisors + 1
print(triNumber)

jhlkshdflaksdcaslidhlfklabl