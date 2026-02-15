def rgb_to_hex(r, g, b):
    """
    Converts an RGB color value to a Hex color string.

    Args:
        r (int): Red component (0-255).
        g (int): Green component (0-255).
        b (int): Blue component (0-255).

    Returns:
        str: The hexadecimal color string (e.g., "#ffffff").
    """
    return "#{:x}{:x}{:x}".format(r, g, b)