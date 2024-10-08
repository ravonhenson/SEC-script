from dotenv import load_dotenv
import os
import sys
import pdfplumber
import gpt
import csv
import pandas
import re

def get_content(filename: str):
    with pdfplumber.open(filename) as pdf:
        content = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            content += page_text if page_text else ""
    return content

def get_title_and_accession_number(filename: str):
    print(filename)
    match = re.search(r"(.+?)\((\d{10}-\d{2}-\d{6})\)\.pdf", filename)
    if match:
        before_accession = match.group(1).strip()  # Part before the accession number
        accession_number = match.group(2)  # The accession number inside parentheses
        return before_accession, accession_number
    else:
        return None, None

load_dotenv()
key = os.getenv("API_KEY")

cd = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(cd, "SEC-filings") # could add a sys argument for the directory
files = [i for i in os.listdir(directory)]
entries = []

bot = gpt.GPT(key)
for file in files:
    entity, accession_number = get_title_and_accession_number(file)
    pdf_path = os.path.join(directory, file)
    # grab that content
    content = get_content(pdf_path)
    # run through chat gpt
    entry = bot.create_entry(accession_number, entity, content) # use createEntry when finished not summary
    entries.append(entry)

with open('output.csv', mode='w', newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(['Accession Number', 'Entity', 'Form', 'Material (T/F)', 'Summary', 'Dollar Amount', 'Record Count', 'Customers Affected'])
    for entry in entries:
        writer.writerow(entry.return_list())

print("ran program")