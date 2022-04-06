class Message:
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2

    def Fuck_you(self):
        return f"Fuck you {self.par1}"

    def Im_sorry(self):
        return f"But I`m sorry for that...{self.par2}"


class Insult(Message):
    def Speak_check(self):
        return "What should we say when somebody disturbs us?"

    def Excuse_check(self):
        return "And what should we say after?"


if __name__ == "__main__":
    message = Insult(input(), input())
    print(message.Speak_check())
    print(message.Fuck_you())
    print(message.Excuse_check())
    print(message.Im_sorry())
