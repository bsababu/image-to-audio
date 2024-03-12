import torch
import requests
# x = torch.rand(5, 3)
# print(x)
from transformers import pipeline

# def tryOne():
#     classifier = pipeline("sentiment-analysis")
#     res = classifier("I have been waiting for to start huggig face course")

#     #Another pipeline example
#     generator = pipeline("text-generation", model="distilgpt2")
#     res1 = generator(
#         "In this course, we will teach you how to",
#         max_length=30,
#         num_return_sequences = 2
#     )


#     #Another zero shot class pipleine

#     classf = pipeline("zero-shot-classification")

#     res2 = classf(
#         "this is the course about the python list comprehension", candidate_labels = [
#             "Ëducation","Politics","business"
#         ]
#     )
#     #print(res2)
#     # summarization

#     summ = pipeline("summarization",model="")
#     txt="""
#         put some texts
#     """
#     #print(summ(txt,max_length=150,min_length=30,do_sample=False))

# HUGGING_FC_TOKEN='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'

# def text_to_gen():
#     API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
#     headers = {"Authorization": f"Bearer {HUGGING_FC_TOKEN}"}

#     def query(payload):
#         response = requests.post(API_URL, headers=headers, json=payload)
#         return response.json()
        
#     output = query({
#         "inputs": "Can you please let us know more details about your ",
#     })

#     return output

# def text_to_audio():
#     headers = {"Authorization": f"Bearer {HUGGING_FC_TOKEN}"}
#     API_URL = "https://api-inference.huggingface.co/models/microsoft/speecht5_tts"

#     def query(payload):
#         response = requests.post(API_URL, headers=headers, json=payload)
#         return response

#     output = query({"text_inputs": "Max is the best doggo."})
#     return output


# if __name__=="__main__" :
#     #print(text_to_gen())
#     print(text_to_audio())