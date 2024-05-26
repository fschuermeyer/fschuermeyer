import feedparser

feed = feedparser.parse("https://hellocoding.de/feed-felix-schuermeyer.xml")

def copyReadme():
  with open("README.template.md", "r") as file:
    data = file.read()

    with open("README.md", "w") as file:
      file.write(data + "\n")

def update():
  copyReadme()

  for entry in feed.entries:
    mdLink = f"- [{entry.title}]({entry.link})"

    with open("README.md", "a") as file:
      file.write(mdLink + "\n")
    
if __name__ == "__main__":
  update()