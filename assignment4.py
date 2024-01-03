class User:
    def __init__(self, id, username, password, email, profile_picture):
        self.id = id
        self.username = username
        self._password = password  # Protected attribute
        self.email = email
        self.profile_picture = profile_picture
        self._posts = []  # Protected list of posts

    def create_post(self, content):
        # Create a new Post object and add it to the user's posts
        post = Post(content, self)
        self._posts.append(post)

    def like_post(self, post_id):
        # Find the post and add the user to its likes
        # ... implementation details

    def get_profile_info(self):
        # Return public profile information
        return {"username": self.username, "profile_picture": self.profile_picture}

    def change_password(self, new_password):
        # Update the password
        self._password = new_password

class RegularUser(User):
    def follow_user(self, user_id):
        # ... implementation details

    def unfollow_user(self, user_id):
        # ... implementation details

class Admin(User):
    def __init__(self, *args, is_super_admin=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_super_admin = is_super_admin

    def promote_user(self, user_id):
        # ... implementation details (super admins only)

    def demote_user(self, user_id):
        # ... implementation details (super admins only)

    def delete_post(self, post_id):
        # ... implementation details

    def ban_user(self, user_id):
        # ... implementation details

class Post:
    def __init__(self, content, author):
        self.id = generate_unique_id()  # Example ID generation
        self.content = content
        self.creation_date = datetime.now()
        self.author = author
        self.likes = []

    def get_author_info(self):
        return self.author.get_profile_info()

    def get_number_of_likes(self):
        return len(self.likes)

    def is_liked_by(self, user_id):
        return user_id in self.likes
