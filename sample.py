from plantDetectionIA import download_gpt, PlantDetection
import os

os.environ["max_split_size_mb"] = "10"
GPTAnswer = input("Download and use the GPT [Y/n]>>>")

if GPTAnswer.lower() == 'y':
    model, specs = download_gpt()
    classify = PlantDetection(dataset='dataset', gpt=model, gpt_specs=specs)
else:
    print("Training a model from dataset/ with 10 epochs")
    classify = PlantDetection(dataset='dataset')
    classify.__device = 'cpu'
    classify.train(10)

print("Welcome to the sample plant detection in image AI.")
image = input("Enter an image filename >>>")

classify(image)
