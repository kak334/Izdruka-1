#[1,2,2,"teksts",3.56,[1,"objekts"]]
my_list = ["STRING", 100, 23.5]
print(my_list)
print(len(my_list))
mylist = ['viens', "divi", "trīs", "četri"]
print(mylist[2])
print(mylist[1:])

cits_list = ["pieci", "seši"]
print(mylist+cits_list)
jauns_list = mylist + cits_list
print(jauns_list)

jauns_list[0] = 1
print(jauns_list)
jauns_list.append("septiņi")
jauns_list.append(8)
print(jauns_list)

jauns_list.pop()

print(jauns_list)

pop_elem=jauns_list.pop()
print(pop_elem)
print(jauns_list)
jauns_list.pop(3)
print(jauns_list)

new_list=["b","a","e","c"]
num_list=[4,1,8,3]
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
new_list.reverse()
print(new_list)
#myList = [1, 2, 3, 100, 'tu', 3.59, 'skaista!']
#myList.sort()
#print(myList)


nested_list = [2,4,[5,8]]
print(len(nested_list))
print(nested_list[1])
print(nested_list[2])
print(nested_list[2][1])

augli = ["ābols", "banāns ","gurķis"]
print(augli[2])
augli[2] = "apelsīns"
print(augli)
augli.append("bumbieris")
print(augli)
augli.insert(2, "citrons")
print(augli)
augli.pop(1)
print(augli)
augli.sort()
print(augli)
print(f"Šaja sarakstā ir {len(augli)} augli.")

