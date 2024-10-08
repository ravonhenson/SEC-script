from dotenv import load_dotenv
import os
import sys
import pdfplumber
import gpt
import csv
import pandas

def get_content(filename: str):
    with pdfplumber.open(filename) as pdf:
        content = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            content += page_text if page_text else ""
    return content

filings = [
    "0000732717-24-000046",
    "0001437749-24-022743",
    "0001437749-24-024679",
    "0001213900-24-031252",
    "0001193125-24-147625",
    "0001193125-24-133132",
    "0001104659-24-028288",
    "0001104659-24-084351",
    "0001562151-24-000032",
    "0001089063-24-000104",
    "0001467623-24-000024",
    "0001654954-24-002505",
    "0000950170-23-072513",
    "0000950170-24-004247",
    "0000950170-23-073848",
    "0001193125-24-100764",
    "0000320335-24-000029",
    "0000045012-24-000052",
    "0001645590-24-000009",
    "0000719733-24-000015",
    "0000719733-24-000035",
    "0000719733-24-000047",
    "0000950170-24-030041",
    "0000950170-24-038881",
    "0000950170-24-089345",
    "0001193125-24-011295",
    "0001193125-24-062997",
    "0001193125-24-094797",
    "0001193125-24-033753",
    "0001193125-24-040749",
    "0000950170-24-033954",
    "0001043509-24-000060",
    "0001043509-24-000063",
    "0000950103-24-002017",
    "0001558370-24-004390",
    "0000731766-24-000045",
    "0000731766-24-000085",
    "0000731766-24-000150",
    "0000950123-23-011228",
    "0001193125-24-010243"
]

load_dotenv()
key = os.getenv("API_KEY")

cd = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(cd, "SEC-filings") # could add a sys argument for the directory
files = [i for i in os.listdir(directory)]
entries = []

bot = gpt.GPT(key)
for accession_number in filings[0:3]:
    #check if accession number in a dir name
    for file in files:
        if accession_number in file:
            pdf_path = os.path.join(directory, file)
            # grab that content
            content = get_content(pdf_path)
            # run through chat gpt
            entry = bot.create_entry(content) # use createEntry when finished not summary
            entries.append(entry)

with open('output.csv', mode='w', newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(['Accession Number', 'Entity', 'Form', 'Material (T/F)', 'Dollar Amount', 'Record Count', 'Customers Affected'])
    for entry in entries:
        writer.writerow(entry.return_list())

print("ran program")