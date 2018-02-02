class User:
    def __init__(self, display_name, user_id, picture_url, status_message):
        self.display_name = display_name
        self.user_id = user_id
        self.picture_url = picture_url
        self.status_message = status_message
    def get_tuple(self):
        return (self.display_name,
                self.user_id,
                self.picture_url,
                self.status_message)

