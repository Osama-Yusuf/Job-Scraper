import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import re

app = Flask(__name__)


@app.route("/")
def index():
    # Create a list to store the job details
    jobs = []

    # Loop through the first 9 pages
    for i in range(0, 10):
        url = f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&filters%5Bcareer_level%5D%5B0%5D=Entry%20Level&filters%5Bcareer_level%5D%5B1%5D=Experienced&q=devops&start={i}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        job_listings = soup.find_all('div', class_='css-pkv5jc')

        # Loop through each job listing
        for job in job_listings:
            title = job.find('a', class_='css-o171kl').text.strip()
            company = job.find('a', class_='css-17s97q8').text.strip()
            location = job.find('span', class_='css-5wys0k').text.strip()
            date_div = job.find('div', class_='css-4c4ojb')
            if date_div:
                date_text = date_div.get_text(strip=True, separator=' ')
                date_list = date_text.split()
                if len(date_list) > 1:
                    date = date_list[0] + ' ' + \
                        date_list[1] + ' ' + date_list[2]
                else:
                    date = "N/A"
            type = job.find('span', class_='css-1ve4b75 eoyjyou0').text.strip()
            url = 'https://wuzzuf.net' + \
                job.find('a', class_='css-o171kl')['href']
            description_divs = job.find_all(
                'a', class_=['css-o171kl', 'css-5x9pm1'])
            description = [div.text.strip() for div in description_divs]
            # jobs.append({'title': title, 'company': company, 'location': location, 'date': date, 'type': type, 'description': description, 'url': url})
            jobs.append({'title': title, 'company': company.replace("-", " "), 'location': location,
                        'date': date, 'type': type, 'description': ', '.join(description), 'url': url})
            exclude_words = ('.net', 'javascript', 'java', 'frontend', 'backend', 'full stack',
                             'Frontend Team Leadet [Angular]', 'developer', 'angular', 'Wordpress',
                             'web developer', 'developer', 'ruby on rails', '.NET', 'Back-End', 'windows', 'Linux Administrator', 'Linux engineer')
            # jobs = [job for job in jobs if not any(word in job['title'] for word in exclude_words)]

            # jobs = list(filter(lambda job: not any(word in job['title'] for word in exclude_words), jobs))

            jobs = list(filter(lambda job: not any(re.search(
                r'\b' + word + r'\b', job['title'], re.IGNORECASE) for word in exclude_words), jobs))

            jobs.sort(key=lambda x: x['date'], reverse=False)

    return render_template('index.html', jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True)
