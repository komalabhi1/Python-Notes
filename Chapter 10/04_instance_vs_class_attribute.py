'''INSTANCE ATTRIBUTES
An attribute that belongs to the Instance (object). Assuming the class from the previous
example:
harry.name = "harry"
harry.salary = "30k"   # Adding instance attribute '''


class Employee:
    language = "Python"  # this is a class attribute
    salary = 1500000


komal = Employee()
komal.language = "Javascript"  # this is a instance attribute
print(komal.language, komal.salary)


# ye language me "Javascript " hi print krega
# becauze:
# Note: Instance attributes, take preference over class attributes during assignment & retrival

# When looking up for komal.attribute it checks for the following:
# 1) Is attribute present in object?
# 2) Is attribute present in class?
