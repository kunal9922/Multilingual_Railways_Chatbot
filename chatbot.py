import torch
print(torch.__version__)
"""pipeline: Pipeline is methodology which we can use interfaces and model from hugging face transformer"""

from transformers import pipeline
import pandas as pd

class Bot:
    '''A chatbot that gives information about railways in a single word'''
    def __init__(self, dataSetPath: str):
        # using google's questioning and answering Large Language Model 
        self.tqa = pipeline(task='table-question-answering', model='google/tapas-base-finetuned-wtq')
        
        # Contains railways data into pandas data frame as structured manner
        self.railData = pd.read_csv(dataSetPath)
        self.rwTable = self.railData.astype(str)

    def chat(self, userQuery: str) -> str:
        '''Chat method that takes natural language query parameter 
        and result in a single word'''
        
        if not userQuery:
            return None
        
        botReply = self.tqa(table=self.rwTable,query=userQuery)['answer']
        
        return botReply

# Main code
myRailwaysChatBot = Bot(r'Multilingual_Railways_Chatbot\data\indianRailwaysData.csv')
# Example of the user query
# "from Delhi to Jaipur what is the Train Departure time"
# "provide the ticket price of the train goes from Chennai to Bangalore "
# "what is train arrival time goes from Bangalore to Mysore"
# "tell me the distance from Mumbai to Ahmedabad by train"
# "show the train number goes from Pune to Mumbai"

reply = myRailwaysChatBot.chat("What is the Train Name which operates from Delhi to Jaipur")
print(reply)