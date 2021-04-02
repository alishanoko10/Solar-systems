def main():

    choice ='0'
    while choice =='0':
        print("Welcome to kami")
        print("Press 1 to view our products.")
        print("Press 2 to build your own energy system.")
        print("Press 3 \"Who Are We?\"")


        choice = input ("Please make a choice: ")

        if choice == "3":
            print("Kami means wind Armenian\n")
            print("With the electrical circumstances that the country is crossing by, Kami is opened to provide electricity depending only on nature.\n")
            print("Our technologies are developed by Empirical College of London and University of Twenty.\n")
            print("We are based in Damascus, Ghassani, 4th street.\n")
            print("We will open soon in Lebanon and Iraq.\n")
            print("For more information, contact us: Email: alishan_okomochian@edu.aua.am\n")
            print("Phone :00963977324324\n")
            choice=input("Press 0 to go back to main menu.\n")
        elif choice == "2":
            governate=input("which governorate are you located? (Damascus, Homs, Tartus, Aleppo)\n")
            energy=input("What is the use of the Energy system? (home, shop, factory, institution, lights)\n")
            area=inputNumber("What is your (Home. Shop..) area for where the energy system will be installed? (only numbers)\n")
            well=input("Does the location have a working Well? (answer with y/n)")
            connected=input("Do you want to be still connected on the grid? (answer with y/n)\n")
            calculations(governate,energy,area,well,connected)
        elif choice == "1":
            print("Solar panels\nWind turbines (10 kw up to 20 Mega w)\nBatteries (12V, 200Ah)\n")
            print("Inverters\nDump load\nGenerators (5kw up to 100 kw)\n")
            print("Chargers\nControllers\nEnergy management systems\n")
            print("Street lightening with solar and wind turbine (100w up to 500w)")
            print("For more information, contact us: Email: alishan_okomochian@edu.aua.am\n")
            print("Phone :00963977324324\n")
            choice=input("Press 0 to go back to main menu.\n")
        else:
            print("I don't understand your choice.")



def calculations(governate,energy,area,well,connected):
    if((governate=="Aleppo" or governate=="Damascus") and (energy=="home" or energy=="shop") and well=="n"):
        print("You can only install solar Panels.\n")
        calc=area*10/120
        print(calc)
        print("KW\n")
        if(calc<5):
            price=800
            print("price is 800$")
        if(calc>5 and calc <= 10):
            price=1200
            print("price is 1200$")
        if(calc>10 and calc<=50):
            price=2000
            print("price is 2000$")
        if(calc>50 and calc<=100):
            price=4000
            print("price is 4000$")
        print("2 x 12V batteries= 400 $")
        print("Inverter 250$")
        print("Controller 150$")
        totalcost=400+250+150+price
        print("Total cost=",totalcost)
    elif((governate=="Aleppo" or governate=="Damascus") and (energy=="home" or energy=="shop") and well=="y"):
        print("You can install a hybrid system.\n")
        calc=area*10/120
        print(calc)
        print("KW\n")
        if(calc<5):
            price=500
            print("price is 500$")
        if(calc>5 and calc <= 10):
            price=900
            print("price is 900$")
        if(calc>10 and calc<=50):
            price=1500
            print("price is 1500$")
        if(calc>50 and calc<=100):
            price=3150
            print("price is 3150$")
        print("2 x 12V batteries= 400 $")
        print("Inverter 250$")
        print("Controller 150$")
        totalcost=400+250+150+price
        print("Total cost=",totalcost)
    elif((governate=="homs" or governate=="tartus") and (energy=="home" or energy=="shop")):
        print("You can install both solar system or wind turbine(recommended)\n")
        calc=area*10/120
        print(calc)
        print("KW\n")
        if(calc<5):
            price=800
            print("price is 800$")
        if(calc>5 and calc <= 10):
            price=1200
            print("price is 1200$")
        if(calc>10 and calc<=50):
            price=2000
            print("price is 2000$")
        if(calc>50 and calc<=100):
            price=4000
            print("price is 4000$")
        print("2 x 12V batteries= 400 $")
        print("Inverter 250$")
        print("Controller 150$")
        totalcost=400+250+150+price
        print("Total cost=",totalcost)
    elif(energy=="factory" or energy=="institution"):
        print("please contact us to take an appointment.\n")
        print("Email: alishan_okomochian@edu.aua.am\n")
        print("Phone :00963977324324\n")
        print("We will come and check your location and which System is best for your comfort.\n")
        
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput 
            break 
main()
