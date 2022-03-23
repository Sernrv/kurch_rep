class Message:
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2

    def Fuck_you(self):
        return "Fuck you"

    def Im_sorry(self):
        return "But I`m sorry for that..."


class Insult(Message):
    def Speak_check(self):
        return "What should we say when somebody disturbs us?"
    def Excuse_check(self):
        return "And what should we say after?"


if __name__ == "__main__":
    message = Insult(1, 2)
    print(message.Speak_check())
    print(message.Fuck_you())
    print(message.Excuse_check())
    print(message.Im_sorry())
