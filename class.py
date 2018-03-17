# javascript ES6

# class Hotels{
#     name = "pop"
#
#     getName(){
#         return "chakra kembar"
#     }
# }
#
# const hotel = new Hotels()
# console.log(hotel.name)

# 1. Start class Hotels
class Hotels:
    name = "pop"

    def get_name(self):
        return self.name

    def get_type(self):
        return [
            'syariah',
            'konvensional',
            '+'
        ]

    def rating(self, rating_input):
        return rating_input

    def get_type_syariah(self):
        return self.get_type()[0]

# EOF 1

hotel = Hotels()
print(hotel.name)
print(hotel.get_name())
print(hotel.get_type()[1])
print(hotel.rating(5))
print(hotel.get_type_syariah())
