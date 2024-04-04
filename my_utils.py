# Experiment-5: Create a Python module by defining a few functions and variables and Import the
# module created in step 1 into another Python script and use its functions and variables.

# Creation of Python module
PI = 3.14159

# Greets a person by name.
def greet(name):
  return f"Hello, {name}!"

# Calculates the area of various shapes.
# Supported Shapes:
#    - 'circle': radius
#    - 'rectangle': length, width
#    - 'triangle': base, height (assumes right triangle)
def calculate_area(shape, *args):
  if shape == 'circle':
    return PI * args[0] ** 2
  elif shape == 'rectangle':
    return args[0] * args[1]
  elif shape == 'triangle':
    return 0.5 * args[0] * args[1]
  else:
    raise ValueError(f"Unsupported shape: {shape}")
