<h1 align="center">Safe Chat</h1>

<p align="center">
<img src="https://storage.googleapis.com/kaggle-media/competitions/jigsaw/003-avatar.png" width="96">
<br/>
<b>Intelligent Comment Filtering</b>
<br>
<b><a href="https://huggingface.co/spaces/iperkins/safe_chat">Safe Chat Demo</a><b>
</p>

# About

Safe Chat is a demo project to showcase my `LLM` skills. I iterated through nine models that can be found in the `checkpoints` folder. For each iteration I adjust hyper paramters of an `LSTM` model, but I settled on using a `GRU` due to it being more efficent. I am including a graph of the train and validation loss for each iteration in `graphs`. Additionaly, each models performance can be viewed in `model_metrics.csv`. Training was done using `Google Colab` and data was pulled from `Kaggle`. The final purpose of this project was to learn `Gradio` and `Hugging Face` where I am hosting a demo using this model here: https://huggingface.co/spaces/iperkins/safe_chat

## Installation Instructions
```bash
1. git clone https://github.com/Isaac987/safe_chat
2. cd safe_chat
2. pip install -r requirements.txt
```

## Sources
Kaggle Dataset: https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge

Youtube Reference: https://www.youtube.com/watch?v=ZUqB-luawZg
