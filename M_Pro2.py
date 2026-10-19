students = input("Enter student names: ").lower().split()

hash_table = {}

for name in students:
    hash_table[name] = hash_table.get(name, 0) + 1

print("\nStudent Name Frequency:")
for name, count in hash_table.items():
    print(name, ":", count)

