from dotenv import load_dotenv, find_dotenv
from transformers import pipeline
import scipy
import streamlit as st
import os
import requests

hugg_api_token = os.getenv("HUGGING_FC_TOKEN")

load_dotenv(find_dotenv())

def imgToTxt(img):
    #img_to_txt = pipeline("image-to-text", model="Salesforce/blip2-opt-2.7b")
    img_to_txt = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base") #task, model
    txt = img_to_txt(img)[0]["generated_text"]
    #print(txt)
    return txt

#imgToTxt("/imgs/anaclet_to_ced.jpeg")

def txt_to_audio(par):
    API_URL = "https://api-inference.huggingface.co/models/suno/bark"
    headers = {"Authorization": f"Bearer {hugg_api_token}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    audio_bytes = query({
        "inputs": par,
    })
    with open("audio.flac",'wb') as fl:
        fl.write(audio_bytes)
    # return audio_bytes
    return audio_bytes

def generate_text(scn):
    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom-560m"
    headers = {"Authorization": f"Bearer {hugg_api_token}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": scn,
    })

    return output

# def txtToSpeech(msg):
#     txt_to_audio = pipeline("text-to-speech",model="suno/bark")
#     speech = txt_to_audio(msg, forward_params={"do_sample": True})
#     scipy.io.wavfile.write("audio_from_txt.wav", rate=speech["sampling_rate"], data=speech["audio"])

def main():
    st.set_page_config(page_title="img to txt",page_icon="👁️‍🗨️")
    st.header("Turn image into story")
    upload_img = st.file_uploader("pick an image..",type="jpeg")
    if upload_img is not None:
        print(upload_img)
        bytes_img = upload_img.getvalue()
        with open(upload_img.name, "wb") as fl:
            fl.write(bytes_img)
        st.image(upload_img,caption="Uploaded 🪭", use_column_width=True)
        scenario = imgToTxt(upload_img.name)
        stry = generate_text(scenario)

        txt_to_audio(stry)
        with st.expander("scenario"): st.write(scenario)
        with st.expander("story"): st.write(stry)
        st.audio("audio.flac")


if __name__=="__main__" :
    main()

#run with streamlist :: streamlit run [name of the file]