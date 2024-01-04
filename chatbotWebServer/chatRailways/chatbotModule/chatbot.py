from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

class Bot:
    '''A chatbot that gives information about railways in the Natural Language 
    by leveraging open source Large Language Models'''
    def __init__(self):
        
        # Load our Trains dataset from the CSV file
        loader = CSVLoader(file_path = r'chatRailways\chatbotModule\data\indianRailwaysData.csv', encoding='utf8', csv_args={'delimiter': ','})
        data = loader.load()

        # Now split the Indian Railways data into chunks so that it cant fit easily into memory
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
        # Tokenizing the data as text chunks
        text_chunks = text_splitter.split_documents(data)
        # download the Sentence Transformer Embedding From Hugging Face
        embeddings = HuggingFaceEmbeddings(model_name=r'sentence-transformers/all-MiniLM-L6-v2')
        # Converting the text chunks into embeddings and saving the embeddings into FAISS Knowledge Base
        self.docSearch = FAISS.from_documents(text_chunks, embeddings)

        # to Save the Vector Embeddings
        DB_FAISS_PATH = r'chatRailways\chatbotModule\data\vectorEmbeddingsFaiss'
        self.docSearch.save_local(DB_FAISS_PATH)
        
        # Chatbot model LLama-2-7B urls to Download (https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) save into the folder "chatRailways\chatbotModule\models"
        self.llm = CTransformers(model=r'chatRailways\chatbotModule\models\llama-2-7b-chat.ggmlv3.q4_0.bin',
                            model_type = 'llama',
                            max_new_tokens = 512,
                            temperature =0.5,
                            )

    def chat(self, userQuery: str) -> str:
        '''Chat method that takes natural language query parameter 
        and results Natural Language Response'''
        
        if not userQuery:
            return None
        
        #         Chain for having a conversation based on retrieved documents.
        # This chain takes in chat history (a list of messages) and new questions, and then returns an answer to that question.
        qa = ConversationalRetrievalChain.from_llm(self.llm, retriever=self.docSearch.as_retriever())

        chat_history = []
        # Passing the user's query to the chatbot 
        botReply = qa({"question": userQuery, "chat_history": chat_history})
        print(botReply["answer"], type(botReply["answer"]))
        return botReply["answer"]