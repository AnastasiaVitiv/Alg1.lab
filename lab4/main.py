from ship import Ship

def main():
    ship1 = Ship(15555, "Leonard", 555, "Lui", 55, 2444)
    ship2 = Ship(27777, "Di", 777, "Devid", 77, 455)
    ship3 = Ship(32222, "Caprio", 222, "Lui", 22, 99)
    ship4 = Ship()


    ship4.speed = 3333

    ship_array = [ship1, ship2, ship3, ship4]

    min_ship = ship_array[0]
    for ship in ship_array:
        if ship.getDistance() < min_ship.getDistance():
            min_ship = ship

    print(f"Корабель з мінімальним пробігом: {min_ship}")

    del ship1

if __name__ == "__main__":
    main()
