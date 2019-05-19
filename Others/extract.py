import re

m1 = []
m2 = []
m3 = []

r1 = []
r2 = []
r3 = []

with open("results.csv") as results:
  for each_line in results:
    if each_line.startswith("Movie1SoldOutTime"):
      m1.append(float(re.split(",+", each_line)[1]))
    if each_line.startswith("Movie2SoldOutTime"):
      m2.append(float(re.split(",+", each_line)[1]))
    if each_line.startswith("Movie3SoldOutTime"):
      m3.append(float(re.split(",+", each_line)[1]))
    if each_line.startswith("Record Reneging Movie1 Customers"):
      r1.append(float(re.split(",+", each_line)[1]))
    if each_line.startswith("Record Reneging Movie2 Customers"):
      r2.append(float(re.split(",+", each_line)[1]))
    if each_line.startswith("Record Reneging Movie3 Customers"):
      r3.append(float(re.split(",+", each_line)[1]))
    else:
      continue
print()
print()
for e in m1:
  print(e)
print()
print()
for e in m2:
  print(e)
print()
print()
for e in m3:
  print(e)
print()
print()
for e in r1:
  print(e)
print()
print()
for e in r2:
  print(e)
print()
print()
for e in r3:
  print(e)
print()
print()