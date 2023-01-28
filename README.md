# Job Scraper

Job Scraper is a Python script that scrapes job listings from the website "Wuzzuf.net" and stores them in a list of dictionaries. Each dictionary contains the following information about a job listing:
- Title
- Company
- Location
- Date
- Type
- Description

## Features
- Scrapes job listings from the website "Wuzzuf.net"
- Excludes job listings with certain keywords in the title (".net", "javascript", "java", "frontend", "backend", "full stack", "developer", "angular", "Wordpress", "web developer", "developer", "ruby on rails")
- Sort the date from new to old 

## Usage
1. Clone the repository to your local machine
    ```bash
    git clone https://github.com/Osama-Yusuf/Job-Scraper.git
    ```
2. Navigate to the project directory
    ```bash
    cd Job-Scraper
    ```
3. Install the required packages using pip: 
    ```bash
    pip3 install -r requirements.txt
    ```
4. Run the script using Python: 
    ```bash
    python3 job_scraper.py
    ```
5. Now Open the browser and go to the following link: 
    ```bash
    http://localhost:5000/
    ```
