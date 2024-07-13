import webbrowser

fav_links = [
    "https://www.google.com/",
    "https://eg.linkedin.com/",
    "https://www.facebook.com/",
    "https://copilot.microsoft.com/",
]

def firefox(link):
    webbrowser.open(link)