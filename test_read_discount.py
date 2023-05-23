
from proj08 import read_discount

fp = open("discount_small.csv",encoding='UTF-8')
print("discount_small.csv")
instructor = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
              'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0}

print("Instructor:")
print(instructor)
student = read_discount(fp)
print("Student:")
print(student)

assert student == instructor
print("\n"+"-"*20)
fp = open("discount_medium.csv",encoding='UTF-8')
print("discount_medium.csv")
instructor = {"Tom Clancy's Rainbow Six Siege": 60.06, "No Man's Sky": 50.03, \
              'SCUM': 50.07, 'X4: Foundations': 60.03, 'SkiFy': 50.0, 'X3: Reunion': 53.0, \
                  'XCOM: Enemy Unknown': 75.05, 'Crazy Machines 3': 90.18, \
                      "Assassin's Creed�: Director's Cut Edition": 70.14, 
                      'Trine 2: Complete Story': 75.04, 'Tom Clancy�s Splinter Cell Blacklist': 75.08, \
                          'Road Redemption': 70.13, 'The Room Three': 60.27, 'Hello Neighbor': 80.11, \
                              'Mirror': 60.0, 'Trine Enchanted Edition': 75.16, 'Trine 3: The Artifacts of Power': 75.13}


print("Instructor:")
print(instructor)
student = read_discount(fp)
print("Student:")
print(student)

assert student == instructor