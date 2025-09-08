import feedparser

companies = ["Tesla", "Apple", "Google", "Microsoft"]

for company in companies:
    print(f"\n--- News headlines for {company} ---\n")

    # Google News RSS feed
    url = f"https://news.google.com/rss/search?q={company}"
    feed = feedparser.parse(url)

    if feed.entries:
        for i, entry in enumerate(feed.entries[:10], start=1):  # Limit to 10 headlines
            print(f"{i}. {entry.title}")
    else:
        print("No headlines found.")
