class GearModule:

    def __init__(self, module, num_teeth) -> None:
        self.module = module
        self.num_teeth = num_teeth

    def pitch_diameter(self):
        return self.module * self.num_teeth

    def outside_diameter(self):
        return self.module * (self.num_teeth + 2)

    def root_diameter(self):
        return self.module * (self.num_teeth - 2.5)

    def addendum(self):
        return self.module

    def dedendum(self):
        return 1.25 * self.module

    def circular_pitch(self):
        import math
        return math.pi * self.module

    def base_diameter(self):
        from math import cos, radians
        pressure_angle = 20  # Assuming standard pressure angle
        return self.module * self.num_teeth * cos(radians(pressure_angle))

    def tooth_thickness(self):
        from math import pi
        return pi * self.module / 2
