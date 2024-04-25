import wikipedia

user_input = input(">>: ")

while user_input != "":
    page = wikipedia.summary(user_input)
    print(page)
    print("Title:", page.title)
    print("Summary:", page.summary)
    print("URL:", page.url)
    user_input = input(">>: ")
