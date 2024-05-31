#list ichidagi elementni indeksini chiqarish va count

soz = ["banana", "monitor", "planshet", "cap", "onion", "sumka", "laptop", "phone"]
print(soz)
target = input("So'zni kiriting: ")
count = 0
for i in soz:
    count += 1
    if i == target:
        print(i)
        break
index = soz.index(target)
print(f"""
          so'z: {target}.
          index: {index}.
          count:{count}.""")
