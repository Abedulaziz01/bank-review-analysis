📱 Bank App Review Sentiment Analysis

📌 Overview

This project analyzes user sentiment and thematic trends in Google Play Store reviews for three major Ethiopian banking apps:

Bank of Abyssinia (BOA)

Commercial Bank of Ethiopia (CBE)

Dashen Bank

The goal is to identify strengths, weaknesses, and opportunities to improve user experience across these apps using Natural Language Processing (NLP) techniques.

🧰 Tools and Technologies

Programming Language: Python

Sentiment Analysis: TextBlob, VADER (NLTK)

Text Preprocessing: spaCy

Keyword Extraction: TF-IDF Vectorizer (scikit-learn)

Data Storage: Oracle Database (used for storing processed and cleaned review data)

Visualization: Matplotlib, Seaborn

Version Control: Git & GitHub

📊 Key Features

Scrapes and preprocesses user reviews from the Play Store

Performs sentiment analysis using TextBlob and VADER

Extracts frequent keywords and highlights context-specific sentiment

Clusters reviews into themes: Account Access, Customer Support, Speed & Performance

Visualizes sentiment distribution, theme frequency, and keyword trends

📁 Project Structure

├── data/ # Raw and cleaned review data
├── notebooks/ # Jupyter notebooks with analysis and visualizations
├── scripts/ # Data scraping, processing, and analysis scripts
├── reports/ # Project report and visual outputs
├── .gitignore # Ignored files and folders
├── requirements.txt # Python dependencies
├── README.md # Project overview and instructions

📊 Preprocessing Summary

Using the Python package google_play_scraper, we scraped 400 reviews for each of the three banks — Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank — totaling 1,200 reviews.

After scraping, the following preprocessing steps were performed:

Duplicate Check:

🔍 Found 10 duplicate reviews based on the combination of review, rating, date, and bank.

✅ All duplicates were successfully removed.

Missing Data Check:

🔎 Checked for missing values in all key columns (review, rating, date, bank, source).

✅ No missing values were found in the dataset.

Date Normalization:

All review dates were normalized to the standard format YYYY-MM-DD for consistency and ease of analysis.

The cleaned dataset is saved as: data/cleaned_reviews.csv.

✅ Total final reviews after cleaning: ~1190 (depending on exact duplicates removed).

🔍 Results Summary

Dashen Bank consistently had the highest positive sentiment across both TextBlob and VADER

BOA showed relatively higher negative sentiment and more complaints about speed and support

CBE had strong neutral and positive reviews, but also notable mentions of access issues

📦 Installation & Setup

# Clone the repository

$ git clone https://github.com/your-username/bank-app-review-analysis.git

# Navigate to project folder

$ cd bank-app-review-analysis

# Create and activate virtual environment

$ python -m venv venv
$ source venv/bin/activate # On Windows: venv\Scripts\activate

# Install dependencies

$ pip install -r requirements.txt

🗄️ Oracle Database

Processed and cleaned reviews were stored in an Oracle Database instance to facilitate scalable access and backup of structured sentiment data. SQL queries were used to fetch categorized review records for visualization and analysis.

🚀 How to Run

Run the scraping script to download Play Store reviews

Execute preprocessing pipeline

Run sentiment analysis and keyword extraction

Generate and view visualizations

Export results to Oracle or local files

🧪 Testing and Validation

Verified sentiment results using sample reviews

Compared TextBlob vs. VADER outputs for consistency

Reviewed top keywords and themes for alignment with ratings

📃 License

This project is licensed under the MIT License.

👨‍💻 Author

Abdulaziz MohammedProject Team Lead | Data & AI SpecialistAddis Ababa, Ethiopia

🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📬 Contact

For more information, reach out via GitHub or LinkedIn.
