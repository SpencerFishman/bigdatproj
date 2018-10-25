class NFLTeam:
    def __init__(self,city,mascot,lat,long,):
        self.city = city
        self.mascot = mascot
        self.latitude = lat
        self.longitude = long
        self.fullName = "{},{}".format(city,mascot)

    def __repr__(self):
        return ("The {} {} are located at {} N {} W".format(self.city,self.mascot,self.latitude,self.longitude))

