from bs4 import BeautifulSoup
import requests 
import csv
from itertools import zip_longest
import pandas as pd

result = requests.get("https://wuzzuf.net/search/jobs/?a=navbl&filters%5Bcountry%5D%5B0%5D=Saudi%20Arabia&filters%5Bpost_date%5D%5B0%5D=within_1_week&q=data%20analyst")
src = result.content

soup = BeautifulSoup(src, "lxml")


job_titles = [title.text for title in soup.find_all("h2", class_="css-m604qf")]
locations = [location.text for location in soup.find_all("span", class_="css-5wys0k")]
company_names = [name.text for name in soup.find_all("a", class_="css-17s97q8")]
job_skills = [desc.text for desc in soup.find_all("div", class_="css-y4udm8")]
date_posted = [date.text for date in soup.find_all("div", class_="css-4c4ojb")]


jobs_data = zip(job_titles, locations, company_names, job_skills, date_posted )

#Naming The Excel sheet columns
df = pd.DataFrame({
    "Job Title": job_titles,
    "Location": locations,
    "Company Name": company_names,
    "Job skills": job_skills,
    "Date Posted": date_posted,
 
})

file_path = r"C:\Users\WG\Documents\jobs.xlsx" 
# Save the DataFrame to an Excel file
df.to_excel(file_path, index=False)

print("Data written to jobs.xlsx")
