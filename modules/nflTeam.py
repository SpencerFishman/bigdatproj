class NFLTeam:
    def __init__(self,city,mascot,lat,long,):
        self.city = city
        self.mascot = mascot
        
        self.fullName = self.city + self.mascot
        self.latitude = lat
        self.longitude = long
        if mascot == 'FortyNiners':
            self.fullName = "{} 49ers".format(city)
        else:
            self.fullName = "{} {}".format(city,mascot)

    def __repr__(self):
        return ("The {} {} are located at {} N {} W".format(self.city,self.mascot,self.latitude,self.longitude))

