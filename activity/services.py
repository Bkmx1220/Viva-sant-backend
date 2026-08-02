ACTIVITY_CALORIES_PER_MINUTE = {
    "walking": 4,
    "running": 10,
    "cycling": 8,
    "swimming": 9,
    "yoga": 3,
    "gym": 6,
}


def calculate_calories(activity_type, duration):
    """
    Calcule les calories brûlées.
    """
    calories_per_minute = ACTIVITY_CALORIES_PER_MINUTE.get(activity_type, 0)

    return round(calories_per_minute * duration, 2)