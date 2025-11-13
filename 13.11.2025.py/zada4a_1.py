# 1. Задвоить элементы в списке. То есть компьютер превращает список [4, print, "xyz", None] в список [4, 4, print, print, "xyz", "xyz", None, None]
element_1 = [4, "sunny", "xyz", "snow"]
new = []

element_1.insert(1, "4")
print(element_1)

element_1.insert(3, "sunny")
print(element_1)

element_1.insert(5, "xyz")
print(element_1)

element_1.insert(7, "snow")
print(element_1)

new.extend(element_1)

del element_1
print(new)
 

 