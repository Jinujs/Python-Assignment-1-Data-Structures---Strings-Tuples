string1 = "Hello "
string2 = input("Enter your Name: ")

output = string1 + string2
print(output)

string3 = ", welcome to Python programming"
result = output + string3

print(result)

print("First character:", result[0])
print("Last character:", result[-1])
print("First 5 characters:", result[:5])
print("Last 11 characters:", result[-11:])
print("Reversed string:", result[::-1])
print("Python:", result[23:29])

strM = "Python beginner tutorial"
print("Uppercase:", strM.upper())
print("Lowercase:", strM.lower())
print("Capitalize:", strM.capitalize())
print("Count of 't':", strM.count('t'))
print("Replace:", strM.replace("Python", "Machine Learning"))

t1 = (10, 20, 30)
t2 = (40, 50, 60)
t_combine = t1 + t2
print("Combined tuple:", t_combine)
print("Repeated tuple:", t_combine * 3)
print("3rd element:", t_combine[2])
print("First three elements:", t_combine[:3])
print("Last three elements:", t_combine[-3:])