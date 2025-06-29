# Before optimization
is_admin = True
is_logged_in = True

if is_admin == True and is_logged_in == True:
    print("Вітаємо, адміністратор!")


# After optimization
is_admin = True
is_logged_in = True

if is_admin and is_logged_in:
    print("Вітаємо, адміністратор!")
