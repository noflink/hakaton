class Host:
    def __init__(self, host_dict):
        self.host_id = host_dict["host_id"]
        self.name = host_dict["name"]
        self.family_name = host_dict["family_name"]
        self.email = host_dict["email"]
        self.password = host_dict["password"]
        self.id = host_dict["id"]
        self.address = host_dict["address"]
        self.phone_number = host_dict["phone_number"]