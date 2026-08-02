def calculate_bmi(height, weight):
    """
    Calcule l'IMC.
    height : cm
    weight : kg
    """
    if not height or not weight:
        return None

    height_m = height / 100
    return round(weight / (height_m ** 2), 2)


def bmi_category(bmi):
    """
    Retourne la catégorie de l'IMC.
    """
    if bmi is None:
        return None

    if bmi < 18.5:
        return "Insuffisance pondérale"
    elif bmi < 25:
        return "Poids normal"
    elif bmi < 30:
        return "Surpoids"
    elif bmi < 35:
        return "Obésité modérée"
    elif bmi < 40:
        return "Obésité sévère"

    return "Obésité morbide"


def daily_water(weight):
    """
    Besoin quotidien en eau (35 ml/kg).
    """
    if not weight:
        return 0

    return int(weight * 35)