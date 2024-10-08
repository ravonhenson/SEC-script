import os
import sys
import pdfplumber
from dotenv import load_dotenv

import openai
from openai import OpenAI

def main() -> None: 
    if len(sys.argv) > 1:
        accession_number = sys.argv[1]
        print(f"Accession Number: {accession_number}") 
    else:
        print("Please enter accession number.")
        sys.exit();

    load_dotenv()
    key = os.getenv("API_KEY")

    cd = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(cd, "SEC-filings") # could add a sys argument for the directory

    files = [i for i in os.listdir(directory)]
    content = "" 
    match = next((i for i in files if accession_number in i), None)

    # load entries from directory

    # take ts and export it
    export(arr, "test.csv")

if match is None:
    print("There is no filing with that accession number in my local dataset.")
else:
    with pdfplumber.open(f"{directory}/{match}") as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                content += text

    client = OpenAI(api_key=key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are summarizing the text for a cybersecurity report."},
            {
                "role": "user",
                "content": f"Summarize this text in 2-3 sentences: {content}"
            }
        ]
    )

    print(completion.choices[0].message.content)

def export(arr: list, filename: str) -> None:
    

if __name__ == "__main__":
    main()