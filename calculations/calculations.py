from gears.gear_module import GearModule
from gears.gear_diametral_pitch import GearDiametralPitch


def calculate_module(module, num_teeth):
    gear = GearModule(module, num_teeth)
    return {
        "Diámetro Primario": gear.pitch_diameter(),
        "Diámetro Exterior": gear.outside_diameter(),
        "Diámetro del Fondo": gear.root_diameter(),
        "Addendum": gear.addendum(),
        "Dedendum": gear.dedendum(),
        "Paso Circular": gear.circular_pitch(),
        "Diámetro Base": gear.base_diameter(),
        "Espesor del Diente": gear.tooth_thickness()
    }


def calculate_diametral_pitch(diametral_pitch, num_teeth):
    gear = GearDiametralPitch(diametral_pitch, num_teeth)
    return {
        "Diámetro Primario": gear.pitch_diameter(),
        "Diámetro Exterior": gear.outside_diameter(),
        "Diámetro del Fondo": gear.root_diameter(),
        "Addendum": gear.addendum(),
        "Dedendum": gear.dedendum(),
        "Paso Circular": gear.circular_pitch(),
        "Diámetro Base": gear.base_diameter(),
        "Espesor del Diente": gear.tooth_thickness()
    }
