import numpy as np


def calculate(list_input):
    """Hitung mean, variance, std, max, min, sum dari matriks 3x3.

    Args:
        list_input (list): list berisi 9 angka.

    Returns:
        dict: statistik untuk axis 0, axis 1, dan flattened.

    Raises:
        ValueError: bila list tidak berisi tepat 9 angka.
    """
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list_input).reshape(3, 3)

    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.flatten().mean().tolist(),
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.flatten().var().tolist(),
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.flatten().std().tolist(),
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.flatten().max().tolist(),
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.flatten().min().tolist(),
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.flatten().sum().tolist(),
        ],
    }

    return calculations
