hydration_levels = {"arc1": 23, "arc2": 64, "arc3": 104}


def saturation_levels(data_dict):
    return {key: (value ** 3) / (2 ** value) for key, value in data_dict.items()}


print(f'Saturation Levels: {saturation_levels(hydration_levels)}')
