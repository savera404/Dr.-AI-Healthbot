import os
import base64
import streamlit as st
from groq import Groq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
##set up groq llm api key
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")


##covert image to required format
#image_path='image.png'
def encode_img(image_path):
    image_file=open(image_path,'rb')
    #encoding to prevent file corruption- bit to str
    encoded_img=base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_img

@st.cache_resource
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

@st.cache_resource
def get_faiss_db():
    embedding_model = get_embedding_model()
    DB_FAISS_PATH = 'vectorstore/faiss_store'
    return FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)

@st.cache_resource
def get_groq_client():
    return Groq()

##set up multimodel llm
#query="What happened to my skin"
def analyze_img_n_query(encoded_img,query):

    client = get_groq_client()  # Use cached client
    model="meta-llama/llama-4-scout-17b-16e-instruct"
    caption_prompt="""
    Based on the given image, suggest the most likely disease in 3-8 words. Avoid listing multiple conditions.
    """
    messages=[{
        "role":"user",
        "content":[{
            "type":"text",
            "text": caption_prompt + query
        },
        {
            "type":"image_url",
            "image_url":{
                "url":f"data:image/jpeg;base64,{encoded_img}",
            },

        },
        ]
    }]

    caption_response = client.chat.completions.create(messages=messages, model=model)
    disease_caption = caption_response.choices[0].message.content.strip()
    combined_query = f"{query}. Based on image, disease appears to be: {disease_caption}"

    #change the first response into an embedding
    embedding_model = get_embedding_model()
    query_embedding = embedding_model.embed_query(combined_query)


    #load vector database
    db = get_faiss_db()


    #similarity search first response and vector store
    docs = db.similarity_search_by_vector(query_embedding, k=3)
    context = "\n\n".join([doc.page_content for doc in docs]) 

    #call the model again
    prompt=f""" 
    You are an AI doctor, you are given image and you have to recognize the disease or problem, also give some
    remedies, precautions or possible treatments. Give your answer as a paragraph and do not include special
    characters in your answer. Do not repeat the prompt or query in your answer, start your answer right away 
    without any preambles. If the information about the disease or problem is absent in the Context, answer to
    best of your knowledge. Dont say "Based on the context provided"
    User complaint: {query}
    Suspected disease from image: {disease_caption}
    Supporting medical context: {context}"""
    final_message=[{
        "role":"user",
        "content":[{
            "type":"text",
            "text": prompt
        }
        ]
    }]

    final_chat_completion=client.chat.completions.create(
        messages=final_message,
        model=model
    )

    final_result=final_chat_completion.choices[0].message.content
    return final_result