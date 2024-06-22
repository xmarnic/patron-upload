def flatten_user(user_record, library, profile, alt_id_prefix):
    usr = f"""*** DOCUMENT BOUNDARY ***
FORM=LDUSER
.USER_CHG_HIST_RULE. NOHISTORY
.USER_LIBRARY. {library}
.USER_PROFILE. {profile}
.USER_ID. {user_record['id']}
.USER_ALT_ID. {alt_id_prefix}{user_record['alt_id']}
.USER_FIRST_NAME. {user_record['first_name']}
.USER_LAST_NAME. {user_record['last_name']}
"""
    if "middle_name" in user_record:
        usr += f".USER_MIDDLE_NAME. {user_record['middle_name']}\n"

    # build address portion
    adr = f""".USER_ADDR1_BEGIN.
.STREET. {user_record['street_1']}
.CITY/STATE. {user_record['city']}, {user_record['state']}
.ZIP. {user_record['zip_code']}
.EMAIL. {user_record['email']}
.PHONE. {user_record['home_phone']}
"""
    if "cell_phone" in user_record:
        adr += f".CELLPHONE. {user_record['cell_phone']}\n"
    if "street_2" in user_record:
        adr += f".APT/SUITE. {user_record['street_2']}\n"
    adr += ".USER_ADDR1_END.\n"

    return usr + adr


def flatten_users(users, library, profile):
    alt_id_prefix = "CW" if library == "CWC" else "CC"
    return [flatten_user(user, library, profile, alt_id_prefix) for user in users]
