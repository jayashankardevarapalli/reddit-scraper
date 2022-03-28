import pandas as pd
import praw

reddit = praw.Reddit(
    client_id="0UKhmLGKI40wrx8L-MsG3w",
    client_secret="Z9EjltfCzH6ZByeym7j2UdHsY0lzXA",
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
)


def m(ui,nl):
    data = []
    ui_sr = reddit.subreddit(ui) 
    for dat in ui_sr.hot(limit=nl):
        data.append([dat.id, dat.name, dat.score, dat.title,dat.url,dat.selftext])
    data = pd.DataFrame(data,columns=['id','name','score','title','url','body'])
    fn = input("\nEnter the filename: ")
    data.to_excel(fn+".xlsx")
    print("\n\nJob Done!!\n")



print("\n\t\tReddit Scrapper!!\t\t\n")
print("\nList of categories: \n")
print("\n1.new\t 2.hot\t 3.top\t 4.rising\t 5.exit\n")
ui = input("\nEnter the topic to scrape: ")
nl = int(input("\nEnter the number of threads You want: "))
while True: 
    uo = input("\nEnter the category: ")
    if uo == "new" or uo == "top" or uo == "hot" or uo == "rising":
        m(ui,nl)
    elif uo == "exit":
        break
    else:
        print("\n\tInvalid.....,try again!!")

print("\n\nBye!!!")



