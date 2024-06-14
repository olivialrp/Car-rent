import os

cars = [("Chevrolet Tracker", 120),
        ("Chevrolet Onix", 90),
        ("Chevrolet Spin", 150),
        ("Hyundai HB20", 85),
        ("Hyundai Tucson", 120),
        ("Fiat Uno", 60),
        ("Fiat Mobi", 70),
        ("Fiat Pulse", 130)]

rented = []

def shows_cars_lits(cars_lists):
    for i, car in enumerate(cars_lists):
        print("[{}] {} - R$ {} /day".format(i, car[0], car[1]))

shows_cars_lits(cars)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("----------")
    print("welcome to the car rent shop")
    print("----------")
    print("what do you wish to do?")
    print("0 - show portfolio | 1 - rent a car | 2 - return a car")
    op = int(input())

    os.system("cls" if os.name == "nt" else "clear")
    if op == 0:
        shows_cars_lits(cars)

    elif op == 1:
        shows_cars_lits(cars)
        print("-------")
        print("type the car code you wish to rent")
        car_code = int(input())
        print("for how manyu days you wish to rent the car?")
        days = int(input())
        os.system("cls" if os.name == "nt" else "clear")

        print("you chose {} for {} days".format(cars[car_code][0], days))

        print("the total rent would be R$ {}. Do you wish to proceed and rent?".format(days * cars[car_code][1]))

        print("Type '0' to YES | Type '1' to NO")
        confirmation = int(input())
        if confirmation == 0:
            print("congratulations! you rented {} for {} days".format(cars[car_code][0], days))
            rented.append(cars.pop(car_code))



    elif op == 2:
        if len(rented) == 0:
            print("no cars to return")
        else:
            print("this is the list of rented cars. wich one would you like to return?")
            shows_cars_lits(rented)
            print("")
            print("type the car code you wish to return:")
            code = int(input())
            if confirmation == 0:
                print("thanks for returning the car {}".format(rented[code][1]))
                cars.append(rented.pop(code))

    print("")
    print("---------")
    print("Type '0' to continue | Type '1' to quit")
    if float(input()) == 1:
        break