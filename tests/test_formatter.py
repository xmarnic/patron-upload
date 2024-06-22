import pytest
from formatter import flatten_user, flatten_users

user_record1 = {
    "id": "123456789123456",
    "alt_id": "123456",
    "first_name": "John",
    "middle_name": "Mark",
    "last_name": "Doe",
    "street_1": "123 Elm St",
    "street_2": "Apt 1A",
    "city": "Casper",
    "state": "WY",
    "zip_code": "82601",
    "home_phone": "307-555-4321",
    "cell_phone": "307-555-1234",
    "email": "john.doe@example.com",
}

expected_result1 = """*** DOCUMENT BOUNDARY ***
FORM=LDUSER
.USER_CHG_HIST_RULE. NOHISTORY
.USER_LIBRARY. CSPC
.USER_PROFILE. 25ST
.USER_ID. 123456789123456
.USER_ALT_ID. CC123456
.USER_FIRST_NAME. John
.USER_LAST_NAME. Doe
.USER_MIDDLE_NAME. Mark
.USER_ADDR1_BEGIN.
.STREET. 123 Elm St
.CITY/STATE. Casper, WY
.ZIP. 82601
.EMAIL. john.doe@example.com
.PHONE. 307-555-4321
.CELLPHONE. 307-555-1234
.APT/SUITE. Apt 1A
.USER_ADDR1_END.
"""

user_record2 = {
    "id": "123456789123456",
    "alt_id": "123456",
    "first_name": "John",
    "last_name": "Doe",
    "street_1": "123 Elm St",
    "city": "Casper",
    "state": "WY",
    "zip_code": "82601",
    "home_phone": "307-555-4321",
    "email": "john.doe@example.com",
}
expected_result2 = """*** DOCUMENT BOUNDARY ***
FORM=LDUSER
.USER_CHG_HIST_RULE. NOHISTORY
.USER_LIBRARY. CSPC
.USER_PROFILE. 25ST
.USER_ID. 123456789123456
.USER_ALT_ID. CC123456
.USER_FIRST_NAME. John
.USER_LAST_NAME. Doe
.USER_ADDR1_BEGIN.
.STREET. 123 Elm St
.CITY/STATE. Casper, WY
.ZIP. 82601
.EMAIL. john.doe@example.com
.PHONE. 307-555-4321
.USER_ADDR1_END.
"""


@pytest.mark.parametrize(
    "user_record, library, profile, alt_prefix_id, expected_result",
    [
        (user_record1, "CSPC", "25ST", "CC", expected_result1),
        (user_record2, "CSPC", "25ST", "CC", expected_result2),
    ],
)
def test_flatten_user(user_record, library, profile, alt_prefix_id, expected_result):
    assert flatten_user(user_record, library, profile, alt_prefix_id) == expected_result


def test_flatten_users():
    user_records = [user_record1, user_record2]
    expected_results = [expected_result1, expected_result2]
    assert flatten_users(user_records, "CSPC", "25ST") == expected_results
