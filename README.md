# Flatten-Users

## Introduction

`flatten-users` is a command-line tool designed to streamline the process of
uploading new patrons into the SirsiDynix Symphony Integrated Library System (ILS).
The tool reads an Excel file containing patron data and converts it into an LDUSER
flat file format. This flat file is then used to batch upload new patrons into the
Symphony system.

## Getting Started

To use `flatten-users`, you'll need Python installed on your system along with the necessary Python libraries listed in `requirements.txt`. Follow these steps to set up and run the tool:

1. Clone the repository to your local machine.
2. Navigate to the cloned directory and run:

## Usage

To run `flatten-users`, use the command line to execute the tool with required
parameters. Here's the basic command structure:

    flatten-users -i PATH_TO_INPUT -l LIBRARY_CODE -p USER_PROFILE -o OUTPUT_PATH

## Excel Data Format

### Column Name Detection

`flatten-users` attempts automatically identify columns in the input Excel file by
matching column names to a predefined list of known headers. The tool is designed to
recognize both standard and several non-standard column names to accommodate
variations in column header names.

If the tool cannot determine all required columns based on the column names provided
in the spreadsheet, it will fail gracefully and output a message listing the
unrecognized column names. This will allow you to identify which columns need to be
renamed.

The `flatten-users` tool requires specific fields to be present in the input Excel file. Below, you will find a list of both required and optional fields, along with their default column names that should be used if the tool cannot automatically determine the correct columns.

### Required Fields

Ensure these columns are present in your Excel file with the following default names
if the original names are not recognized:

- **ID** (Unique identifier for the patron)
  - Default column name: `bar`
- **Alternative ID** (Alternative identifier like a student or employee ID)
  - Default column name: `sid`
- **First Name** (First name of the patron)
  - Default column name: `fname`
- **Last Name** (Last name of the patron)
  - Default column name: `lname`
- **Email** (Email address of the patron)
  - Default column name: `email`
- **Home Phone** (Home phone number of the patron)
  - Default column name: `phone`
- **Street Address 1** (Primary address line)
  - Default column name: `street`
- **City** (City of the address)
  - Default column name: `city`
- **State** (State of the address)
  - Default column name: `st`
- **Zip Code** (Zip code of the address)
  - Default column name: `zip`

### Optional Fields

These fields are not mandatory but can be included for more detailed records. Use
the following default names if necessary:

- **Middle Name** (Middle name of the patron)
  - Default column name: `mname`
- **Cell Phone** (Cell phone number of the patron)
  - Default column name: `cell`
- **Street Address 2** (Secondary address line such as an apartment or suite number)
  - Default column name: `apt`
