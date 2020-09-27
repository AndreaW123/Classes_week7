'''Name: Andrea Napoli-Wilson
Class: CIS
Date: 9-26-2020'''

class Vehicle:
    '''defines the basic attributes of a vehicle'''
    def __init__(self, make, model, color, fueltype, options):
        self.make = make
        self.model = model
        self.color = color
        self.fueltype = fueltype
        self.options = options

    def getMake(self):
      return self.make

    def getModel(self):
      return self.model

    def getColor(self):
      return self.color

    def getFuelType(self):
      return self.fueltype

    def info(self):
            print(f'Currently in your garage you have a {self.make} {self.model} and it is {self.color} and has {self.options}')


class Car(Vehicle):
    def __init__(self, make, model, color, fueltype, options, engineSize, numDoors):
        super().__init__(make, model, color, fueltype, options)
        self.engineSize = engineSize
        self.numDoors = numDoors

    def getEngineSize(self):
      return self.engineSize

    def getNumDoors(self):
      return self.numDoors

    def info(self):
      super().info()
      print(f'Engine size: {self.getEngineSize()}, Number of doors: {self.getNumDoors()}')

class PickupTruck(Vehicle):
    def __init__(self, make, model, color, fueltype, options, cabStyle, bedLength):
        super().__init__(make, model, color, fueltype, options)
        self.cabStyle = cabStyle
        self.bedLenth = bedLength

    def getCabStyle(self):
      return self.cabStyle

    def getBedLength(self):
      return self.bedLenth
    
    def info(self):
      super().info()
      print(f'Cab style: {self.getCabStyle()}, Bed length: {self.getBedLength()}')



def printMenu():
  print("Welcome Andrea's Awesome Virtual Garage")

  print("[1] Add a Car")
  print("[2] Add a Pick up Truck")
  print("[3] Show me my Super Cool Garage")
  print("[4] Quit")

  return int(input("Please choose an option from the menu: "))

def selectOptions():
  options_selected = []
  options_available = ['power windows', 'power locks', 'power mirrors', 'dual climate control', 'memory seats', 'cruise control', 'bluetooth', 'remote start']

  while (True):
    for option in options_available:
      print(f'{option}')
    option_chosen = input("Please choose an option to add or enter DONE when you are finish selecting the options: ")
    if (option_chosen.upper() == "DONE"):
      break
    else:
      options_selected.append(option_chosen)

  return options_selected


def getCarInput():
  carDetails = {}
  carDetails["make"] = input("What is the make? ")
  carDetails["model"] = input("What is the model? ")
  carDetails["color"] = input("What is the color? ")
  carDetails["fuelType"] = input("What is the fuel type? ")
  carDetails["options"] = selectOptions()
  carDetails["engineSize"] = input("What is the engine size? ")
  carDetails["numDoors"] = input("How many doors? ")
  return carDetails

def getPickupTruckInput():
  PickupTruckDetails = {}
  PickupTruckDetails["make"] = input("What is the make? ")
  PickupTruckDetails["model"] = input("What is the model? ")
  PickupTruckDetails["color"] = input("What is the color? ")
  PickupTruckDetails["fuelType"] = input("What is the fuel type? ")
  PickupTruckDetails["options"] = selectOptions()
  PickupTruckDetails["cabStyle"] = input("What is the cab style? ")
  PickupTruckDetails["bedLength"] = input("What is the bed length? ")
  return PickupTruckDetails

def showGarage(garage):
  for vehicle in garage:
    #print(f'{vehicle.getMake()} {vehicle.getModel()} {vehicle.getColor()} {vehicle.getFuelType()}')
    #vehicle.printOptions()
    vehicle.info()

def main():
  garage = []
  while (True):
    garageOption = printMenu()

    if (garageOption == 1):
      vehicleDetails = getCarInput()
      car = Car(vehicleDetails["make"],
                    vehicleDetails["model"],
                    vehicleDetails["color"],
                    vehicleDetails["fuelType"],
                    vehicleDetails["options"],
                    vehicleDetails["engineSize"],
                    vehicleDetails["numDoors"])

      garage.append(car)
      print("Vehicle added\n")
    elif (garageOption == 2):
      vehicleDetails = getPickupTruckInput()
      PickupTruck = PickupTruck(vehicleDetails["make"],
                    vehicleDetails["model"],
                    vehicleDetails["color"],
                    vehicleDetails["fuelType"],
                    vehicleDetails["options"],
                    vehicleDetails["cabStyle"],
                    vehicleDetails["bedLength"])

      garage.append(PickupTruck)
      print("Vehicle added\n")
    elif (garageOption == 3):
      if (len(garage) == 0):
        print("You currently have no cars or trucks in Andrea's Awesome Virtual Garage")
      else:
        showGarage(garage)
    elif (garageOption == 4):
      print("Thanks for using Andrea's Awesome Virtual Garage builder it was great to have you!. ")
      break
    else:
      print("Invalid option, please try again")

    input("Press any number key to continue...")

main()
