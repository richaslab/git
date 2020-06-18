#Classes and Instances
#why should we use classes
#logically regroup data 

class Employee:
    pass

#difference between Class
#Class is a blueprint for creating instances

emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

#OUTPUT
"""
<__main__.Employee object at 0x00CB1D30>
<__main__.Employee object at 0x00CB1CF0>
"""
#Instance variables 
emp_1.first = "Arunima"
emp_1.last = 'Dhar'
emp_1.email = 'xyz@gmail.com'

