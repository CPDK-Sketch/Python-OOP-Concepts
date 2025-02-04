class Bird:
    def sound(self):
        return "Some sound"

class Sparrow(Bird):
    def sound(self):
        return "Chirp chirp"

class Crow(Bird):
    def sound(self):
        return "Caw caw"

birds = [Sparrow(), Crow()]
for bird in birds:
    print(bird.sound())
