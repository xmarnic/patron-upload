import sys
import pandas as pd

"""
These are the are standard names of the required fields. Each required field
must be mapped to a known column name in the input spreadsheet.
"""
required_fields = {
    "id",
    "alt_id",
    "first_name",
    "last_name",
    "email",
    "home_phone",
    "street_1",
    "city",
    "state",
    "zipcode",
}

"""
Map standard field names to a list of non-standard known column names that have
been found in the input spreadsheets. Standard field names have a many-to-one
relationship with known column names.
"""
standard_name_to_known_headers = {
    "id": ["bar", "Library Barcode", "W71 ID Card Number"],
    "alt_id": ["sid", "Employee ID", "Student ID", "Person ID"],
    "first_name": [
        "fname",
        "Person Chosen First Name - W72",
        "Person First Name",
    ],
    "middle_name": ["mname", "Person Middle Name"],
    "last_name": [
        "lname",
        "Person Chosen Last Name - W72",
        "Person Last Name",
    ],
    "email": [
        "email",
        "Staff Email",
        "Student Email",
        "Person Preferred Email Address",
    ],
    "cell_phone": ["cell", "Cell Phone"],
    "home_phone": ["phone", "Home Phone", "Person Phone Number"],
    "street_1": ["street", "Person Address Line 1"],
    "street_2": ["apt", "Person Address Line 2"],
    "city": ["city", "Person Address City"],
    "state": ["st", "Person Address State"],
    "zipcode": ["zip", "Person Address Zip"],
}


def map_known_headers_to_standard_name():
    """
    Map known non-standard speadsheet column names to standard field names.
    """
    column_map = {}
    for standard_name, known_headers in standard_name_to_known_headers.items():
        for known_header in known_headers:
            column_map[known_header] = standard_name
    return column_map


def standardize_headers(df):
    """
    Standardize the column headers by renaming any non-standard headers fournd
    in the input spreadsheet to the appropriate standard field name. If all
    required fields are not found, the missing fileds are printed and the
    program exits.
    """
    known_headers = map_known_headers_to_standard_name()
    headers_found = set()
    for column in df.columns:
        if column in known_headers:
            headers_found.add(known_headers[column])
            df.rename(columns={column: known_headers[column]}, inplace=True)

    if missing_required := required_fields - headers_found:
        print(f"Missing required columns: {missing_required}")
        sys.exit(1)


def extract_users(df):
    """
    Extract data from the input spreadsheet and return a list of dictionaries,
    where each dictionary represents a row in the input spreadsheet. The keys
    are standard field names and the values are the corresponding data from the
    input spreadsheet.
    """
    standardize_headers(df)
    return df.to_dict(orient="records")
