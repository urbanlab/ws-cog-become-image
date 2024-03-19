import gradio as gr
import gradio.utils as gr_utils
from gradio_client import utils as client_utils
import requests
from PIL import Image
import base64, binascii
import json
import io


def greet(image, image_to_become, prompt, negative_prompt, number_of_images, denoising_strength, prompt_strength, control_depth_strength, instant_id_strength, image_to_become_strength, image_to_become_noise, seed, disable_safety_checker):
    url = "http://localhost:5000/predictions"
    
    

    image = client_utils.encode_url_or_file_to_base64(image)
    image_to_become = client_utils.encode_url_or_file_to_base64(image_to_become)
  
    payload = json.dumps({
    "input": {
        "image": "https://endpoint-s3.doesnotexist.club/public-bucket/workshop/8368283.jpeg",
        "image_to_become": "https://endpoint-s3.doesnotexist.club/public-bucket/workshop/pAINT_00329_.png",
        "prompt": "a snail hoho",
        "negative_prompt": "",
        "number_of_images": 2,
        "denoising_strength": 1,
        "prompt_strength": 2,
        "control_depth_strength": 0.8,
        "instant_id_strength": 1,
        "image_to_become_strength": 0.75,
        "image_to_become_noise": 0.3,
        "seed": 0,
        "disable_safety_checker": False
    }
    })
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    
    # Send the request with the payload
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print(response.text)
        exit()
        return "lol"

    else:
        # If there's an error, return the status code and error message
        return f"Error {response.status_code}: {response.text}"

# Then, update the iface definition and launch parameters as before


iface = gr.Interface(
    fn=greet,
    inputs=[
        gr.Image(label="Input Image", type="filepath"),
        gr.Image(label="Image to Become", type="filepath"),
        gr.Textbox(label="Prompt"),
        gr.Textbox(label="Negative Prompt"),
        gr.Slider(label="Number of Images", minimum=0, maximum=4, value=1),
        gr.Slider(label="Denoising Strength", minimum=0, maximum=1, value=1),
        gr.Slider(label="Prompt Strength", minimum=0, maximum=2, value=1),
        gr.Slider(label="Control Depth Strength", minimum=0, maximum=1, value=0.8),
        gr.Slider(label="Instant ID Strength", minimum=0, maximum=1, value=1),
        gr.Slider(label="Image to Become Strength", minimum=0, maximum=1, value=0.75),
        gr.Slider(label="Image to Become Noise", minimum=0, maximum=1, value=0.3),
        gr.Number(label="Seed", value=0),
        gr.Checkbox(label="Disable Safety Checker", value=True)
    ],
    outputs=[
        gr.File(label="Output Image")
    ],
    title="Image Transformation",
    description="Transforms an input image based on another image and textual prompts."
)

# Launch the interface
iface.launch(share=True)

