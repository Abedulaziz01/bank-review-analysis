## 📊 Preprocessing Summary

Using the Python package **`google_play_scraper`**, we scraped **400 reviews for each of the three banks** — Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank — totaling **1,200 reviews**.

After scraping, the following preprocessing steps were performed:

1. **Duplicate Check**:

   - 🔍 Found **10 duplicate reviews** based on the combination of `review`, `rating`, `date`, and `bank`.
   - ✅ All duplicates were successfully removed.

2. **Missing Data Check**:

   - 🔎 Checked for missing values in all key columns (`review`, `rating`, `date`, `bank`, `source`).
   - ✅ **No missing values** were found in the dataset.

3. **Date Normalization**:
   - All review dates were normalized to the standard format `YYYY-MM-DD` for consistency and ease of analysis.

The cleaned dataset is saved as: `data/cleaned_reviews.csv`.

✅ Total final reviews after cleaning: **~1190** (depending on exact duplicates removed).
