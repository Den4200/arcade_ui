from typing import Tuple


def check_point_for_collision(
    point: Tuple[float, float],
    left: float,
    right: float,
    bottom: float,
    top: float
) -> bool:
    if left < point[0] < right and bottom < point[1] < top:
        return True
    return False
