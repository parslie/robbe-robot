cmds = dict()


# Command bases 

class Command:
    def __init__(self, name):
        self.name = name


def bind_command(cls: Command):
    instance = cls()
    cmds[instance.name] = instance

# Command definitions

@bind_command
class Test(Command):
    def __init__(self):
        super().__init__('test')