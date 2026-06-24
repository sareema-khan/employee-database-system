#showroom for cars , cycles , motorcycles 
#features 
#add cars
#viwe cars
#serch for cars
#delete car from records 
#update in showroom
# exit 



print("="*40)
print("\t Welcom to Drive ")
print("="*40)

#list with dictionar


cars = [
  {
   "Brand":"Mercedes",
   "Model":"C Class",
   "Color":"Black",
   "Year":"2026",
   "Fuel Type":"Petrol",
   "Price":"20,000,000",
  
 },
   
 {
    "Brand":"BMW",
    "Model": "M4 Competition",
"Color": "Blue",
"Price": "32,000,000",
"Year": "2024",
"Fuel Type": "Petrol",
},
{
    "Brand": "Tesla",
"Model": "Model 3",
"Color": "Red",
"Price": "14,000,000",
"Year":"2024",
"Fuel Type": "Electric",
    
  }
]
#fuction for show car
def show_car():
  car_brand=input("Enter The car Brand : ")
  for car in cars:
  
    if car["Brand"] ==car_brand:
     print("Brand :", car["Brand"])
     print("Model :", car["Model"])
     print("Color :", car["Color"])
     print("Price :", car["Price"])
     print("Year :", car["Year"])
     print("Fuel Type :", car["Fuel Type"])
     break

    else:
      print("Car not FOUND ")
#for motorcycles 
motorcyce = [
  {
   "Brand":"Mercedes",
   "Model":"C Class",
   "Color":"Black",
   "Year":"2026",
   "Fuel Type":"Petrol",
   "Price":"20,000,000",
  
 },
   
 {
    "Brand":"BMW",
    "Model": "M4 Competition",
"Color": "Blue",
"Price": "32,000,000",
"Year": "2024",
"Fuel Type": "Petrol",
},
{
    "Brand": "Tesla",
"Model": "Model 3",
"Color": "Red",
"Price": "14,000,000",
"Year":"2024",
"Fuel Type": "Electric",
    
  }
]
#fuction for show car
def show_motorcyle():
  motorcyce_brand=input("Enter The car Brand : ")
  for car in cars:
  
    if car["Brand"] ==motorcyce_brand:
     print("Brand :", car["Brand"])
     print("Model :", car["Model"])
     print("Color :", car["Color"])
     print("Price :", car["Price"])
     print("Year :", car["Year"])
     print("Fuel Type :", car["Fuel Type"])
     break

    else:
      print("Motorcycle not FOUND ")
while True:
 print("\nAvailable Vechiles")
 print("1.Cars")
 print("2.MotorCycles")
 print("3.Cycles")
 print("4.exit")

 choise = input("Enter your Desired vechile : ")

 if choise == "1":
    show_car()
 else:
   print("Existing ")
   break