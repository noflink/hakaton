class Post:
    def __init__(self, post_id, host_id, host_name,
                 host_family, city, address, spots, available, content):
        self.post_id = post_id
        self.host_id = host_id
        self.host_name = host_name
        self.host_family = host_family
        self.city = city
        self.address = address
        self.spots = spots
        self.available = available
        self.content = content

post = Post(333222, 3333111, "tehila", "zvulunov",
            "ramla", "yosi banai", 3, 3, "dxgfch")


