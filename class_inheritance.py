class Buildings:
    name = "pop"

    def get_color(self):
        return "white"

class Hotels(Buildings):

    # @override
    name = "cakwe"

    def __init__(self):
        self.name = "burger"

    # @??? !PR COBA DICARI
    # name = 1

    rating = 5


hotel = Hotels()
hotel.name = "kwetiaw"
print(hotel.name)
print(hotel.rating)
print(hotel.get_color())
