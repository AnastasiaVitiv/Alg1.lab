class Ship:
    def __init__(self, tonnage=0, name="", passenger_count=0, captain_name="", speed=0, distance=0):
        self.__tonnage = tonnage
        self.__name = name
        self.__passenger_count = passenger_count
        self.captain_name = captain_name
        self.speed = speed
        self.__distance = distance

    def getTonnage(self):
        return self.__tonnage

    def getName(self):
        return self.__name

    def getPassengerCount(self):
        return self.__passenger_count

    def getDistance(self):
        return self.__distance

    def setDistance(self, distance):
        self.__distance = distance




    def __str__(self):
        return (
            f"name={self.__name}; "
            f"tonnage={self.__tonnage}; "
            f"passenger_count={self.__passenger_count}; "
            f"captain_name={self.captain_name}; "
            f"speed={self.speed}; "
            f"distance={self.__distance} "
        )

    def __repr__(self):
        return (
            f"{self.__name}"
            f"{self.__tonnage}"
            f"{self.__passenger_count}"
            f"{self.captain_name}"
            f"{self.speed}"
            f"{self.__distance}"
        )

    def __del__(self):
        print(f"Корабель '{self.__name}' потонув.")

