numbers = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']

numbers.sort(key=len)
new_num = []
for i in numbers:
    if len(i)==4:
        new_num.append(i)
print(new_num)          #['Zero', 'Four', 'Five', 'Nine']

new_num = []
new_num = [n for n in numbers]
print(new_num)          #['One', 'Two', 'Six', 'Zero', 'Four', 'Five', 'Nine', 'Three', 'Seven', 'Eight']
new_num = [len(n) for n in numbers]
print(new_num)          #[3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
#Filteringn condition similar like stream in Java
new_num = [n for n in numbers if len(n)==4]
print(new_num)          #['Zero', 'Four', 'Five', 'Nine']

values = [1,4,5,6,7,4,3,7,9,3]
#printing only duplicate values
print([n for n in values if n%2==0])    #[4, 6, 4]