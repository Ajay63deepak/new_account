#function
def listtodict(sort_orders, sorted_dict): 
   sorted_dict = dict(sort_orders) 
   return sorted_dict 

#input
data = {'ajay':100 , 'mylesh':900 , 'rahul': 300 , 'vinoth':500 , 'kowshe':700}
print (data)

#declared variable
replace_key  = input ("enter the key :")
replace_value = int(input ("enter the value :"))
sorted_dict = {}

#adding new value
new_dict = {replace_key : replace_value}
data.update(new_dict)
print (data)

#sorting the dictionary
sort_orders = sorted(data.items(), key=lambda x: x[1]) #it create's a list of tuples for sorting
print (sort_orders) 

#converting list to dictionary
sorted_dict = listtodict(sort_orders,sorted_dict)
print (sorted_dict)

#removing the min value
to_be_removed = str(min(sorted_dict))
sorted_dict.pop(to_be_removed)
print (sorted_dict)