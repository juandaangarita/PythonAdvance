my_set = {3, 4, 5}
print('my_set= ', my_set)

my_set2 = {'Hola', 23.3, False, True}
print('my_set2= ', my_set2)

my_set3 = {3, 3, 2}
print('my_set3= ', my_set3)

#Esto da un error porque la lista es mutable y el set solo puede recibir elementos inmutables
# my_set4 = {[1, 2, 3], 4}
# print('my_set4= ', my_set4)

my_list = [1, 1, 2, 3, 4, 4, 5]
my_set5 = set(my_list)
print(my_set5)

my_tuple = ('Hola', 'Hola', 'Hola', 1)
my_set6 = set(my_tuple)
print(my_set6)

# To add items to a set
my_set6.add(4)
print(my_set6)

#Adding multiples elements
my_set6.update([1, 2, 5])
print(my_set6)
my_set6.update({14,2,30}, (1, 4, 9), 'Prueba')
print(my_set6)

#Deleting elements remove only delete existing elements, discard can delete an element even if there is not in the set.
my_set6.discard(7)
print(my_set6)

my_set6.remove(1)
print(my_set6)

#This is an erros

# my_set6.remove('Final')

#This erase a random element
my_set6.pop()
print(my_set6)

#Delete the set
my_set6.clear()
print(my_set6)

#union
my_set7 = my_set2 | my_set3
print(my_set7)

#Intersection
my_set8 = my_set2 & my_set3
print(my_set8)

#Diference: Taking elements from set 1 that are contain in set 2
my_set9 = my_set5 - my_set6
print(my_set9)

#Simetric difference: You keep the number that are not contain in common in the set 1 and 2
my_set10 = my_set5 ^ my_set7
print(my_set10)


def remove_duplicates(my_list):
    # without_duplicates = []
    # for element in my_list:
    #     if element not in without_duplicates:
    #         without_duplicates.append(element)
    # return without_duplicates
    return list(set(my_list))

def run():
    random_list = [1, 1, 2, 2, 4]    
    print(remove_duplicates(random_list))
    
    
if __name__ == '__main__':
    run()

