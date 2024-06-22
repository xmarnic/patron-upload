import argparse
import pandas as pd
import sys

from validator import valid_library_codes, valid_user_profiles, is_valid_combination
from extractor import extract_users
from formatter import flatten_users


def main():
    parser = argparse.ArgumentParser(
        description="Create a Load User flat file from an Excel file."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="Path to the Excel file to extract data from",
    )
    parser.add_argument(
        "-l",
        "--library",
        choices=valid_library_codes,
        required=True,
        help=f"Library Code must be one of: {valid_library_codes}",
    )
    parser.add_argument(
        "-p",
        "--profile",
        choices=valid_user_profiles,
        required=True,
        help=f"User Profile must be one of: {valid_user_profiles}",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="patron-load-flat-file",
        help="Path where the output file will be written",
    )
    args = parser.parse_args()

    # validate the combination of library code and user profile
    if not is_valid_combination(args.library, args.profile):
        parser.error(
            f"Invalid combination of library code and user profile: {args.library}, {args.profile}"
        )

    # load the Excel file
    try:
        df = pd.read_excel(args.input, dtype=str).fillna("")
    except FileNotFoundError:
        print(f"File not found: {args.input}")
        sys.exit(1)
    except ValueError:
        print(f"Invalid file type: {args.input}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    # extract the user data
    users = extract_users(df)
    users = flatten_users(users, args.library, args.profile)

    # flatten users and write to the output file
    try:
        with open(args.output, "w") as file:
            for user in users:
                file.write(user)
    except Exception as e:
        print(f"An error occurred while writing the output file: {e}")
        sys.exit(1)
    print(f"Users successfully written to: {args.output}")


if __name__ == "__main__":
    main()
