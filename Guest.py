class Guest:
    def __init__(self, guest_dict):
        self.guest_id = guest_dict["guest_id"]
        self.name = guest_dict["name"]
        self.family_name = guest_dict["family_name"]
        self.email = guest_dict["email"]
        self.password = guest_dict["password"]


