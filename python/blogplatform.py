class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class BlogPlatform:
    def __init__(self):
        self.blog_posts = []

    def create_post(self, post):
        self.blog_posts.append(post)

    def view_posts(self):
        if not self.blog_posts:
            print("No blog posts available.")
        else:
            print("Blog Posts:")
            for i, post in enumerate(self.blog_posts, 1):
                print(f"{i}. {post.title}")
                print(post.content)
                print()

def main():
    blog_platform = BlogPlatform()

    print("Welcome to the Blog Platform App!")

    while True:
        print("\nMenu:")
        print("1. Create Blog Post")
        print("2. View Blog Posts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the blog post: ")
            content = input("Enter the content of the blog post: ")
            post = BlogPost(title, content)
            blog_platform.create_post(post)
            print("Blog post created successfully.")
        elif choice == '2':
            blog_platform.view_posts()
        elif choice == '3':
            print("Thank you for using the Blog Platform App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
