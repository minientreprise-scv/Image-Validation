from imageai.Classification.Custom import ClassificationModelTrainer, CustomImageClassification


class PlantDetection:

    def __init__(self, dataset='dataset', gpt=None, gpt_specs=None):
        self.dataset_folder = dataset
        self.model_trainer = ClassificationModelTrainer()
        self.model_trainer.setModelTypeAsResNet50()
        self.model_trainer.setDataDirectory(f"{dataset}")
        self.prediction = CustomImageClassification()
        self.prediction.setModelTypeAsResNet50()
        if gpt is not None and gpt_specs is not None:
            self.load_model(gpt, gpt_specs)

    def load_model(self, h5_model, model_specs):
        self.prediction.setModelPath(f"{h5_model}")
        self.prediction.setJsonPath(f"{model_specs}")
        self.prediction.loadModel()

    def train(self, epochs: int):
        self.model_trainer.trainModel(num_experiments=epochs, batch_size=10, model_directory=f'{self.dataset_folder}/models')

    def __call__(self, image):
        predictions, probabilities = self.prediction.classifyImage(image, result_count=2)
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(eachPrediction, " : ", eachProbability)
