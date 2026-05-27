y = float(input("Bitte gib Zahl 1 ein: ")) 
x = float(input("Bitte gib Zahl 2 ein: ")) 
c = float(input("Bitte gib Zahl 3 ein: ")) 
v = float(input("Bitte gib Zahl 4 ein: ")) 
b = float(input("Bitte gib Zahl 5 ein: "))

Zahlen = [y,x,c,v,b]

print("sortierte Zahlen:") 
print(sorted(Zahlen))

print("Summe: ") 
print(sum(Zahlen))

print("Durchschintt: ") 
print(sum(Zahlen)/len(Zahlen))

print("größte Zahl:") 
print(max(Zahlen))

print("kleinste Zahl:") 
print(min(Zahlen))
