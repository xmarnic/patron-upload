import pytest
from extractor import extract_users
from extractor.extractor import _map_known_headers_to_standard_name


@pytest.fixture
def expected_headers():
    return {
        "Library Barcode",
        "Person Chosen Last Name - W72",
        "Person Chosen First Name - W72",
        "Employee ID",
        "Staff Email",
        "Student ID",
        "Student Email",
        "Cell Phone",
        "Home Phone",
        "Person Address Line 1",
        "Person Address Line 2",
        "Person Address City",
        "Person Address State",
        "Person Address Zip",
        "Person Phone Number",
        "Person Preferred Email Address",
        "W71 ID Card Number",
        "Person First Name",
        "Person Middle Name",
        "Person Last Name",
        "Person ID",
    }


def test_all_known_headers_are_mapped(expected_headers):
    actual_headers = set(_map_known_headers_to_standard_name().keys())
    missing_headers = expected_headers - actual_headers
    assert not missing_headers, f"Missing headers: {missing_headers}"


def test_extract_users_on_cwc_staff_sheet():
    users = extract_users("../data/cwc-staff-orig.xlsx")
    user = users[0]
    assert user["first_name"] == "Jennifer"
    assert user["last_name"] == "Amend"
    assert user["alt_id"] == "0069715"
    assert user["email"] == "jamend@cwc.edu"
    assert user["cell_phone"] == "307-851-5502"
    assert user["home_phone"] == "307-857-3832"
    assert user["id"] == "29092009555172"
    assert user["street_1"] == "514 Northridge Dr"
    assert user["street_2"] == ""
    assert user["city"] == "Riverton"
    assert user["state"] == "WY"
    assert user["zip_code"] == "82501"


def test_extract_users_on_cwc_student_sheet():
    users = extract_users("../data/cwc-student-orig.xlsx")
    user = users[157]
    assert user["first_name"] == "Alina"
    assert user["last_name"] == "Sheikova"
    assert user["alt_id"] == "0229248"
    assert user["email"] == "as0623@cwc.edu"
    assert user["cell_phone"] == "314-546-2639"
    assert user["home_phone"] == ""
    assert user["id"] == "29101000758014"
    assert user["street_1"] == "PO Box 6944"
    assert user["street_2"] == ""
    assert user["city"] == "Jackson"
    assert user["state"] == "WY"
    assert user["zip_code"] == "83001"


def test_extract_users_on_cspc_sheet():
    users = extract_users("../data/cspc-orig.xlsx")
    user = users[-2]
    assert user["first_name"] == "Rachael"
    assert user["middle_name"] == "Kellen"
    assert user["last_name"] == "Hamilton"
    assert user["alt_id"] == "0368448"
    assert user["email"] == "rachael.hamilton@mycc.caspercollege.edu"
    assert user["home_phone"] == "618-791-8454"
    assert user["id"] == "29099113411198"
    assert user["street_1"] == "606 E Fremont Street Apt 1"
    assert user["street_2"] == ""
    assert user["city"] == "Laramie"
    assert user["state"] == "WY"
    assert user["zip_code"] == "82072-3206"
