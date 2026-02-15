def validate_username(username):
    """
    Validates that a username meets length and character requirements.

    Requirements:
    - Length must be between 5 and 10 characters (inclusive).
    - Must contain only alphanumeric characters.

    Args:
        username (str): The username string to check.

    Returns:
        bool: True if valid, False otherwise.
    """
    if len(username) < 5 or len(username) > 10:
        return False
    if not username.isalnum():
        return False
    return True