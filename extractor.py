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
    "id": ["Library Barcode", "bar", "W71 ID Card Number"],
    "alt_id": ["Student ID", "sid", "Person ID"],
    "first_name": ["Person Chosen First Name - W72", "fname", "Person First Name"],
    "middle_name": ["mname", "Person Middle Name"],
    "last_name": ["Person Chosen Last Name - W72", "lname", "Person Last Name"],
    "email": ["Student Email", "email", "Person Preferred Email Address"],
    "cell_phone": ["Cell Phone", "cell"],
    "home_phone": ["Home Phone", "phone", "Person Phone Number"],
    "street_1": ["Person Address Line 1", "street"],
    "street_2": ["Person Address Line 2", "apt"],
    "city": ["Person Address City", "city"],
    "state": ["Person Address State", "st"],
    "zipcode": ["Person Address Zip", "zip"],
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
