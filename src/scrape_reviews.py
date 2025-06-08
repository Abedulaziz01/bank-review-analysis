from google_play_scraper import reviews
import pandas as pd

# Define the apps and their names
apps = {
    "CBE ": "com.combanketh.mobilebanking",
    "BOA ": "com.boa.boaMobileBanking",
    "Dashn": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():
    rvs, _ = reviews(
        app_id,
        lang='en',
        country='us',
        count=400  # you can adjust to 400+
    )
    for r in rvs:
        all_reviews.append({
            "review": r['content'],
            "rating": r['score'],
            "date": r['at'].date(),
            "bank": bank,
            "source": "Google Play"
        })

# Convert to DataFrame and save
df = pd.DataFrame(all_reviews)
df.to_csv("data/raw_reviews.csv", index=False)