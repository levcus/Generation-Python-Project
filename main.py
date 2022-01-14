from tabulate import tabulate
addEntry = True
db = []
id = 0
headers = ["Employee Name", "Hours Worked", "Pay Rate", "Regular Pay", "OT Pay","Gross Pay", "Fed Tax", "State Tax", "FICA", "Net Pay"]

while addEntry:
  employeeName = input("Employee's first and last names ")
  try:
    workedHours = float(input("How many hours did the employee work? "))
  except:
    print('You have entered an invalid value.')  
    continue

  try:
    payRate = float(input("What is the pay rate? "))
  except:
    print('You have entered an invalid value.')  
    continue
  
  if workedHours > 40:
    regularPay = 40 * payRate
    otPay = (workedHours - 40) * 1.5 * payRate
    grossPay = regularPay + otPay
    fedTax = grossPay * 0.1
    stateTax = grossPay * 0.06
    fica = grossPay * 0.03
    netPay = grossPay - fedTax - stateTax - fica
    db.append([employeeName.title(), workedHours, payRate, regularPay, otPay, grossPay, fedTax, stateTax, fica, netPay])
  else:
    regularPay = 40 * payRate
    otPay = 0
    grossPay = regularPay
    fedTax = grossPay * 0.1
    stateTax = grossPay * 0.06
    fica = grossPay * 0.03
    netPay = grossPay - fedTax - stateTax - fica
    db.append([employeeName.title(), workedHours, payRate, regularPay, otPay, grossPay, fedTax, stateTax, fica, netPay])
  id += 1

  additionalEntry = input("Type any \"key\" to add an additonal entry or hit \"Enter\" to display a report ")

  if additionalEntry == '':
    break

print(tabulate(db, headers=headers, floatfmt=".2f"))  


  