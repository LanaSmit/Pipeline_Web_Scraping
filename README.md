# Netflix Data ETL Pipeline: Python Web Scraping

An ETL pipeline that scrapes Netflix movie and TV data using Python, cleans and transforms it, and loads the results into a PostgreSQL database.

## 1. Install Dependencies

(Optional) Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

Install Python packages

pip install -r requirements.txt
Your requirements.txt should include:
pandas
psycopg2
beautifulsoup4
selenium
webdriver-manager
requests

## 2. Install Google Chrome and ChromeDriver in WSL Ubuntu

Install Chrome

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y
```
Verify Chrome install

```bash
google-chrome –version
```
Selenium automatically installs ChromeDriver through webdriver-manager.

## 3. Set Up PostgreSQL in WSL

Install PostgreSQL

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y
```

Start PostgreSQL

```bash
sudo service postgresql start
```

Enter PostgreSQL terminal

```bash
sudo -u postgres psql
```

Set password for postgres user

Inside SQL terminal:
```bash
ALTER USER postgres WITH PASSWORD 'lana';
\q
Connection string used in main.py:
postgresql://postgres:lana@localhost:5432/postgres
```

## 4. Run the ETL Pipeline

Execute the full ETL pipeline

python main.py

This will:
1.	Extract data from Netflix Top 10 and create netflix_top10.csv
2.	Transform the CSV using Pandas
3.	Load the cleaned data into PostgreSQL table netflix_top10_movies

## 5. Verify Data in PostgreSQL

Open SQL terminal:
```bash
sudo -u postgres psql
```
Run query:
```bash
SELECT * FROM netflix_top10_movies LIMIT 10;
```

##  6. Code Files Overview

extract.py
-	Uses Selenium + BeautifulSoup
-	Scrapes Netflix Top-10 page
-	Saves output to netflix_top10.csv
  
transform.py
-	Normalizes column names
-	Removes numbers from titles
-	Replaces spaces with underscores
  
load.py
-	Creates table if not exists
-	Inserts transformed data into PostgreSQL
  
main.py
-	Runs Extract, transform  and load
-	Executes the complete pipeline end-to-end
<<<<<<< HEAD
=======

>>>>>>> 16607e4 (Updated project files)
