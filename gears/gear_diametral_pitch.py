class GearDiametralPitch:

    def __init__(self, diametral_pitch, num_teeth) -> None:
        self.diametral_pitch = diametral_pitch
        self.num_teeth = num_teeth

    def pitch_diameter(self):
        return self.num_teeth / self.diametral_pitch

    def outside_diameter(self):
        return (self.num_teeth + 2) / self.diametral_pitch

    def root_diameter(self):
        return (self.num_teeth - 2.5) / self.diametral_pitch

    def addendum(self):
        return 1 / self.diametral_pitch

    def dedendum(self):
        return 1.25 / self.diametral_pitch

    def circular_pitch(self):
        import math
        return math.pi / self.diametral_pitch

    def base_diameter(self):
        from math import cos, radians
        pressure_angle = 20  # Assuming standard pressure angle
        return self.num_teeth / self.diametral_pitch * cos(radians(pressure_angle))

    def tooth_thickness(self):
        from math import pi
        return pi / (2 * self.diametral_pitch)
