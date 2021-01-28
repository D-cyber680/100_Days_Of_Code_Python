file1 = open("file1.txt")
file2 = open("file2.txt")
file1_list = [int(n.rstrip("\n")) for n in file1]
file2_list = [int(n.rstrip("\n")) for n in file2]
file1.close()
file2.close()
print(file1_list)
print(file2_list)
result = [n for n in file1_list if n in file2_list]
print(result)

# Write your code above 👆


