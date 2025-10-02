units=int(input("enter the units consumed"))

if units<50:
    amount=units*882.6
    tax=25
elif units<100:
    amount=50*2.6+(units-50)*3.25
    tax=35
 elif units<200:
    amount=50*26
    tax=45
 else:
    amount=50*2.6+50*3.25+(units-200)*8.45
    tax=75

total=amount+tax
print("totall bil is",total)