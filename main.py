import os
import time


def main():
  global totalAmount
  global totalPrice
  global nameList
  global priceList
  global amountList
  totalAmount = int(0)
  totalPrice = float(0)
  nameList = []
  priceList = []
  amountList = []
  exitvar = ""
  while True:
    
    try:
      userinput = int(input("Enter a value 1-4\n 1. Add item\n 2. Show cart\n 3. Remove all items\n 4. Exit\n"))
    except:
      print("Invalid Input")
      continue

    if userinput >= 1 or userinput <= 4:
      if userinput == 1:
        os.system('clear')
        addItem()
        os.system('clear')
      elif userinput == 2:
        os.system('clear')
        showCart()
        clearscreen = input("Press enter to continue")
        os.system('clear')
      elif userinput == 3:
        emptyCart()
        clearscreen = input("Press enter to continue")
        os.system('clear')
      elif userinput == 4:
        exit()
        exitvar =input('Press Enter to exit')
        break
        
        
    
def addItem():
  try:
    nameList.append(str(input("Enter the name of the item: ")))
  except:
    print("Invalid Input")
    return
  try:
    amountList.append(int(input("Enter the amount of the item:")))
  except:
    print("Invalid Input")
    nameList.pop()
    return
  try:
    priceList.append(float(input("Enter the price of the item:")))
  except:
    print("Invalid Input!")
    nameList.pop()
    amountList.pop()
    return
    
  print("Item added!")


def showCart():
  global totalAmount
  global totalPrice
  
  print("Name\t\t\tAmount\t\t\tPrice\t\t\tTotal")
  for i in range(len(nameList)):
    print(nameList[i], "\t\t\t\t", amountList[i], "\t\t\t\t", priceList[i], "\t\t\t", amountList[i] * priceList[i])
    totalPrice += amountList[i]*priceList[i]
    totalAmount += amountList[i]
  print("Total: $", totalPrice)
  print("Total amount of items: ", totalAmount)
  totalPrice = 0
  totalAmount = 0


def emptyCart():
  nameList.clear()
  amountList.clear()
  priceList.clear()
  print("\nCart emptied!")

def exit():
  global totalAmount
  global totalPrice
  
  print("Thank you for shopping with us!")
  for i in range(len(nameList)):
    totalPrice += amountList[i]*priceList[i]
  print("Total: $", totalPrice)
  totalPrice = 0
  totalAmount = 0
  return


main()