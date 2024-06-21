valid_library_codes = {"CSPC", "CWC"}
valid_user_profiles = {"25ST", "28FS", "28ST"}
valid_combinations = {"CSPC": ["25ST"], "CWC": ["28FS", "28ST"]}


def is_valid_library_code(library_code):
    """
    Returns True if the library code is valid, False otherwise
    """
    return library_code in valid_library_codes


def is_valid_user_profile(user_profile):
    """
    Returns True if the user profile is valid, False otherwise
    """
    return user_profile in valid_user_profiles


def is_valid_combination(library_code, user_profile):
    """
    Returns True if the combination of library code and user profile is valid,
    False otherwise. Assumes that the library code and user profile are valid.
    """
    return user_profile in valid_combinations[library_code]
