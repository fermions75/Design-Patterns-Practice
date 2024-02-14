from abc import ABC, abstractmethod

class Command:
    @abstractmethod
    def execute(self):
        pass

# concrete command classes
class LightOnCommand(Command):

    def __init__(self, light_obj):
        self.light_obj = light_obj
    
    def execute(self):
        self.light_obj.turn_on()

class LightOffCommand(Command):

    def __init__(self, light_obj):
        self.light_obj = light_obj

    def execute(self):
        self.light_obj.turn_off()


# receiver class
class Light:

    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

# invoker class
class RemoteControl:

    def __init__(self, command_obj):
        self.command_obj = command_obj
    
    def press_button(self):
        self.command_obj.execute()

if __name__ == "__main__":
    light = Light()
    light_on = LightOnCommand(light)
    remote = RemoteControl(light_on)
    remote.press_button()