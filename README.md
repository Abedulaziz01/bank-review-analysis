# Bank Reviews Analysis – Task 1: Data Collection & Preprocessing

## 📌 Objective

Scrape Google Play Store reviews for three banks, preprocess the data to prepare it for sentiment or other downstream analysis, and manage the project using Git and GitHub.

---

## ✅ Task Overview

### Git Setup

- Repository created and initialized with `.gitignore` and `requirements.txt`.
- All development done in `task-1` branch with frequent, meaningful commits.

### Web Scraping

- Tool used: `google-play-scraper`
- Scraped the following fields for each review:  
  `review`, `rating`, `date`, `bank`, `source`
- Target: **400+ reviews per bank** (total 1,200+ reviews)

#### 🔢 Number of Reviews Scraped per Bank

| Bank      | Count    |
| --------- | -------- |
| CBE       | 400      |
| BOA       | 400      |
| Dashn     | 400      |
| **Total** | **1200** |

---

## 🧹 Preprocessing

- Removed duplicates
- Handled missing data
- Normalized date format to `YYYY-MM-DD`

### ✅ Missing Data Summary (Before Cleaning)

| Column | Missing Values |
| ------ | -------------- |
| review | 0              |
| rating | 0              |
| date   | 0              |
| bank   | 0              |
| source | 0              |

✔ **No missing values were found** – dataset was already clean.

---
