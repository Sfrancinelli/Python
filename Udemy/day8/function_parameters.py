def greet_with(name, location): # Parameters
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Sebastián","Buenos Aires") # Positional arguments
greet_with(location="Buenos Aires", name="Sebastián") # Keyword arguments

# name --> parameter & "Sebastián" --> argument