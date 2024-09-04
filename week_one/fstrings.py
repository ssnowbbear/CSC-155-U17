total = sum([1,2,3])
#sum = max(3,7) <- Bad variable name
#print(sum)
total2 = sum([1,2,3])
#print(total2)

#DONT NAME VARIABLES AS PYTHON FUNCTIONS!
#TRY NOT TO START VARIABLES WITH UNDERSCORES
#CAN NOT START A VARIABLE WITH A NUMBER

four_totals = 5 #<-- OKAY TO USE

thisIsCamelCase = "sdkfj;als"
thisisnotcamelcase = "asdlkfj" #<---Use underscores over capitals, dont do this
#Always start variable with a lowercase
#Try not to use l I and 1
#Try to avoid O and 0
#Pay attention to typos
#Scroll through list with arrows, accept option with tab

thisIsCamelCase #selected with arrows and tab
thisisnotcamelcase #selected with arrows and tab

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name} was awesome"
print(full_name)

first_name = "Alan"
last_name = "Turing"
full_name = f"{first_name} {last_name}"
print(full_name)

number = 2 * float(input("how many did you want?")) #float will give a decimal, int will not
treat = input("what is your favorite treat") #flip with previous line to make sense
print(f"cool i'll go get some {number} {treat}")
