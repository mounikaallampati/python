def hello(to="world"):
    print("hello",to)
# function with no parameters takes deafault value as world
hello()
name=input("what's your name?")
# function with name parameter overrides default value with name value
hello(name)

# note:in python if we want to call a function it has to be existed before its called in case if you not defining main method.