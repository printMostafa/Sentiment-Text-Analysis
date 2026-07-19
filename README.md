# 📊 Sentiment Text Analysis Engine

A flexible, lightweight Natural Language Processing (NLP) tool developed in Python. This project is capable of performing dual-source text extraction—either by **scraping and auto-summarizing articles directly from the web** or **reading local text files**—and then evaluating the overall emotional tone through **Sentiment Analysis**.

---

## ✨ Features

*   **Web Scraping & Extraction:** Automatically downloads web articles (like Wikipedia or news sites), strips away HTML/ads, and extracts clean body text.
*   **AI Auto-Summarization:** Utilizes Natural Language Processing algorithms to generate a concise summary of long web articles before analysis.
*   **Local File Processing:** Seamlessly switches to reading and analyzing local `.txt` documents for rapid, offline testing.
*   **Polarity Scoring:** Evaluates emotional tone on a precise mathematical scale from `+1.0` (highly positive) to `-1.0` (highly negative), with `0.0` representing completely neutral text.

---

## 🛠️ Tech Stack & Dependencies

This project is built using **Python 3.10+** and relies on the following core libraries:
*   [TextBlob](https://textblob.readthedocs.io/) - For Lexicon-based sentiment tracking.
*   [Newspaper4k](https://github.com/codelucas/newspaper) - For advanced web scraping, article parsing, and text curation.
*   [NLTK](https://www.nltk.org/) - Natural Language Toolkit providing essential linguistic tokenizers.
*   `lxml_html_clean` - To support secure, modern HTML parsing on current Python versions.

---

## 🚀 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME|

## Install Required Libraries
  Run the following command in your terminal to install all modern, compatible dependencies:
  
  Bash
  pip install textblob newspaper4k nltk lxml_html_clean

 ## 📖 How to Run & Configure
The application is structured to handle inputs from two distinct modes. You can customize the source inside main.py:

Mode A: Analyzing Local Text Files (Default Setup)
Create or open a file named Text.txt in the root directory of the project.

Type or paste your custom sentences inside it (e.g., I love this project, it works great!).

Execute the script:

Bash
python main.py
Mode B: Scraping and Analyzing Web Articles
Open main.py and uncomment the newspaper lines.

Provide your target URL variable (e.g., url = 'https://en.wikipedia.org/wiki/Mathematics').

Make sure to feed the extracted article.summary into the TextBlob constructor.

Run the script to see a live web summary and its corresponding sentiment score.

## 🧠 Code Architecture Breakdown
article.download() & article.parse(): Sends HTTP requests, fetches the raw page layout, isolates the main text content, and drops irrelevant sidebars.

article.nlp() & article.summary: Tallies word frequencies and uses scoring heuristics to pinpoint sentences that contain the highest density of key informational weight.

blob.sentiment.polarity: Breaks down the text string into localized tokens, checks them against an integrated sentiment dictionary, and outputs the average score.

##📄 License
This project is open-source and available under the MIT License. Feel free to fork, modify, and distribute it as you see fit!
