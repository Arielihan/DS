from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I've been waitimg for a HuggingFace course my whole life")
print(res)