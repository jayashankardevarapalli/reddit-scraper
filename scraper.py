import praw

reddit = praw.Reddit(
    client_id="0UKhmLGKI40wrx8L-MsG3w",
    client_secret="Z9EjltfCzH6ZByeym7j2UdHsY0lzXA",
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
)



def cat(cate):
    if cate == "new":
        print("Printing New Reddit's!!\n")
        cate_posts = reddit.subreddit('Hacking').new(limit=10)
    elif cate == "hot":
        print("Printing Hot Reddit's!!\n")
        cate_posts = reddit.subreddit('Hacking').hot(limit=10)
    elif cate == "top":
        print("Printing Top Reddit's!!\n")
        cate_posts = reddit.subreddit('Hacking').top(limit=10)
    elif cate == "rising":
        print("Printing Rising Reddit's!!\n")
        cate_posts = reddit.subreddit('Hacking').rising(limit=10)
    for post in cate_posts:
        print(post.title)
        

print("\n\t\tReddit Scrapper!!\t\t\n")
print("\nList of categories: 1)new, 2)hot, 3)top, 4)rising\n")
while True:
    cate = input("Enter the categeory: ")
    if cate == "new" or cate == "hot" or cate == "top" or cate == "rising":
        cat(cate) 
    else:
        print("\tInvalid....")

