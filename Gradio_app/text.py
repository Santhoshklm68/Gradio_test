import gradio as gr
import os
import google.generativeai as palm

palm.configure(api_key = 'AIzaSyD9H4uvO-hgt91JJb_DT4PP6_7SqQr6jy8')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def get_completion(prompt):
    completion = palm.generate_text(
        model = model,
        prompt = prompt,
        temperature = 0,
        max_output_tokens = 50000,
    )
    response = completion.result
    return(response)


iface = gr.Interface(fn=get_completion, inputs=[gr.Textbox(label="Insert code snippet", lines=5)], 
                     outputs=[gr.Textbox(label="Explain here", lines=5)], title="SS code explainer")

iface.launch(share=True)

iface.close()

