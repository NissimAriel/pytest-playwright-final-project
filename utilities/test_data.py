

test_data_for_valid_login = [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
]

test_data_for_not_valid_login = [

("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("", "", "Epic sadface: Username is required"),
    ("wrong_username", "", "Epic sadface: Password is required"),
    ("wrong_username", "wrong_username", "Epic sadface: Username and password do not match any user in this service"),

]



