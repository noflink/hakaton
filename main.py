import database as db


def main():
    db.start()


def start_connection():
    # start gui
    # welcome screen
    # log in & sign up
    # check log in / sign up
    # main screen (guest/host)

    #search function

    #
    pass

def check_login_info(email, password, usertype):
    success = db.check_login(email, password, usertype)
    if success:
        pass
    return

def check_sign_in_info(email, usertype):
    success = db.check_sing_up_email(email, usertype)
    if success:
        add_user(usertype)
    return

def add_user(usertype):
    pass


# post = Post(333222, 3333111, "tehila", "zvulunov",
#             "ramla", "yosi banai", 3, 3, "dxgfch")





if __name__ == '__main__':
    main()


