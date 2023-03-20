import math
import datetime


def decHourJoin(inH: int, inM: int, inS: int) -> float:
    """Join hour, minutes, seconds, timezone integer to hour float.

    Args:
        - inH (int): hour
        - inM (int): minutes
        - inS (int): seconds
    Returns:
        float: hour in float format
    """

    dh = float(inH)
    dm = float(inM) / 60
    ds = float(inS) / 3600
    output = dh + dm + ds
    return output


def degreeDiff(a: float, b: float) -> float:
    """Calculate the difference between two degrees.

    Args:
        - a (float): first degree
        - b (float): second degree

    Returns:
        float: difference between a and b
    """

    out = float()
    if a > b:
        out = a - b
    if a < b:
        out = b - a
    if out > 180.0:
        out = 360.0 - out
    return out


def offsetToTz(datetime_offset: datetime.timedelta) -> float:
    """Convert datetime offset to float in hours.

    Args:
        - datetime_offset (datetime.timedelta): datetime offset

    Returns:
        - float: offset in hours
    """

    # days to hours
    dh = float(datetime_offset.days * 24)
    # seconds to hours
    sh = float(datetime_offset.seconds / 3600.0)
    # total hours
    output = dh + sh
    return output


def sliceToX(slice: int, radius: float, offset: int) -> float:
    """
    Calculates the x-coordinate of a point on a circle based on the slice, radius, and offset.

    Args:
        - slice (int): An integer value that represents the
            slice of the circle to calculate the x-coordinate for.
            It must be an integer value between 0 and 11 (inclusive).
        - radius (float): A float value representing the radius of the circle.
        - offset (int): An integer value that represents the offset in degrees.
            It must be an integer value between 0 and 360 (inclusive).

    Returns:
        float: The x-coordinate of the point on the circle.

    Example:
        >>> import math
        >>> sliceToX(3, 5, 45)
        2.5000000000000018
    """

    plus = (math.pi * offset) / 180
    radial = ((math.pi / 6) * slice) + plus
    return radius * (math.cos(radial) + 1)


def sliceToY(slice: int, r: float, offset: int) -> float:
    """
    Calculates the y-coordinate of a point on a circle based on the slice, radius, and offset.

    Args:
        - slice (int): An integer value that represents the slice of the circle to calculate
            the y-coordinate for. It must be an integer value between 0 and 11 (inclusive).
        - r (float): A float value representing the radius of the circle.
        - offset (int): An integer value that represents the offset in degrees.
            It must be an integer value between 0 and 360 (inclusive).

    Returns:
        float: The y-coordinate of the point on the circle.

    Example:
        >>> import math
        >>> __sliceToY(3, 5, 45)
        -4.330127018922194
    """
    plus = (math.pi * offset) / 180
    radial = ((math.pi / 6) * slice) + plus
    return r * ((math.sin(radial) / -1) + 1)
