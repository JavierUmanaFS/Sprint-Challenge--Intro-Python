# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base Class
class Vehicle:
  pass

# Sub Base Class
class FlightVehicle(Vehicle):
  pass

# Sub Class
class Starship(FlightVehicle):
  pass

# Sub Class
class Airplane(FlightVehicle):
  pass

# Sub Base Class
class GroundVehicle(Vehicle):
  pass

# Sub Class
class Car(GroundVehicle):
  pass

# Sub Class
class Motorcycle(GroundVehicle):
  pass

