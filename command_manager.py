from commands import *

commands = [
    {
        "name": "dummy-1",
        "description": "Dummy command",
        "function": dummy_function
    },

    {
        "name": "dummy-1",
        "description": "Dummy command Dos",
        "function": d
    }
]

def executeCommand(command_name):
    for command in commands:
        if command["name"] is command_name:
            command["function"]()
            break