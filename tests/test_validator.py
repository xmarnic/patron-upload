import pytest

from validator import (
    valid_library_codes,
    valid_user_profiles,
    valid_combinations,
    is_valid_library_code,
    is_valid_user_profile,
    is_valid_combination,
)


def test_is_valid_library_code_with_valid_library_codes():
    for library in valid_library_codes:
        assert is_valid_library_code(library)


def test_is_valid_user_profile_with_valid_user_profiles():
    for profile in valid_user_profiles:
        assert is_valid_user_profile(profile)


def test_is_valid_combination_with_valid_combinations():
    for library, valid_profiles in valid_combinations.items():
        for profile in valid_profiles:
            assert is_valid_combination(library, profile)


def test_is_valid_combination_with_invalid_combinations():
    for library in valid_library_codes:
        for profile in valid_user_profiles:
            if profile not in valid_combinations[library]:
                assert not is_valid_combination(
                    library, profile
                ), f"Combination {library}, {profile} should be invalid but passed."
