from openai import OpenAI
from enum import Enum
import entry

class GPT: 
    
    class Context(Enum):
        CYBERSEC = "You are analyzing the text for a cybersecurity report. Do not exceed 2 sentences under any circumstance."

    class Question(Enum):
        FORM = "What type of filing is this?"
        SUMMARY = "Summarize this text in 2-3 sentences"
        MATERIAL = "Is this event declares as material or non-material (T/F)?"
        DOLLAR_AMOUNT = "What was the dollar amount caused from the incident? (N/A if not applicable)"
        RECORD_COUNTS = "How many record accounts? (N/A if not applicable)"
        NUMBER_OF_CUSTOMERS_AFFECTED = "How many customers were affected by this event? (N/A if not applicable)"

    def __init__(self, key: str):
        self.key = key
        self.client = OpenAI(api_key=key)

    def create_entry(self, accession_number, entity, content: str) -> entry.Entry:
        Entry = entry.Entry(
            accession_number,
            entity,
            self.get_form(content),
            self.material(content),
            self.summary(content),
            self.dollar_amounts(content),
            self.record_counts(content),
            self.num_customers_affected(content)
        )
        return Entry
    
    def get_form(self, content):
        return self.ask("Answer with only the form type.", self.Question.FORM.value, content)
    
    def summary(self, content: str) -> str:
        return self.ask(self.Context.CYBERSEC.value, self.Question.SUMMARY.value, content)
    
    def material(self, content): 
        return self.ask("Your response should only be True or False.", self.Question.MATERIAL.value, content)
    
    def num_customers_affected(self, content): 
        return self.ask("Your response should only include the number of customers affected. If it is not applicable, then say N/A", self.Question.NUMBER_OF_CUSTOMERS_AFFECTED.value, content)
    
    def record_counts(self, content): 
        return self.ask("Your response should only include the record count. If it is not applicable, then say N/A", self.Question.RECORD_COUNTS.value, content)
    
    def dollar_amounts(self, content): 
        return self.ask("Your response should only include the dollar amount. If it is not applicable, then say N/A", self.Question.DOLLAR_AMOUNT.value, content)

    def ask(self, context: str, question: str, content: str, model="gpt-4o-mini", temperature = 0.3) -> str:
        try:
            completion = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": context},
                    {
                        "role": "user",
                        "content": f"{question}: {content}"
                    }
                ],
                temperature=temperature
            )
            #return completion.choices[0].message.content
            return completion.choices[0].message.content
        except Exception as e:
            return f"An error occured: {str(e)}"
        
    

