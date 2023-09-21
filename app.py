import torch
from transformers import pipeline
from PIL import Image
import matplotlib.pyplot as plt
import io

detector50 = pipeline(model="TuningAI/DETR-BASE_Marine")

import gradio as gr

fdic = {
    "style" : "italic",
    "size" : 10,
    "color" : "red",
    "weight" : "bold"
}
labels_ = { "LABEL_0":"None" , "LABEL_1": "Boat" ,"LABEL_2": "Car" ,"LABEL_3" :  "Dock" , "LABEL_4" : "Jetski" ,"LABEL_5" : "Lift"}
def get_figure(in_pil_img, in_results):
    plt.figure(figsize=(16, 10))
    plt.imshow(in_pil_img)
    ax = plt.gca()

    for prediction in in_results:
        selected_color ="#008000"

        x, y = prediction['box']['xmin'], prediction['box']['ymin'],
        w, h = prediction['box']['xmax'] - prediction['box']['xmin'], prediction['box']['ymax'] - prediction['box']['ymin']
        ax.add_patch(plt.Rectangle((x, y), w, h, fill=False, color=selected_color, linewidth=3))
        ax.text(x, y, f"{labels_[prediction['label']]}: {round(prediction['score']*100, 1)}%", fontdict=fdic)

    plt.axis("off")

    return plt.gcf()


def infer(in_pil_img):
    results = detector50(in_pil_img)

    figure = get_figure(in_pil_img, results)

    buf = io.BytesIO()
    figure.savefig(buf, bbox_inches='tight')
    buf.seek(0)
    output_pil_img = Image.open(buf)

    return output_pil_img


with gr.Blocks(title="DETR Object Detection") as demo:
    with gr.Row():
        input_image = gr.Image(label="Input image", type="pil")
        output_image = gr.Image(label="Output image with predicted instances", type="pil")
    gr.Examples(["1.jpg" , "5.jpg"], inputs=input_image)
    send_btn = gr.Button("start")
    send_btn.click(fn=infer, inputs=input_image, outputs=[output_image])
demo.launch(debug=True)
