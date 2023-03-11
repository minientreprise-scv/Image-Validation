# Is there a plant in this image ?
It's the question that this python package can answer. This package can recognize if there is a plant in a photo. It also recognizes soils to be sure that the AI also detect seedling. 

This repository is part of minientreprise-csv 's project. It provides a python package that say if there is a plant in a given image.

## Documentation

### Use in your own project
```shell
pip install plantDetectionIA
```

[//]: # (TODO finish doc)

### Develop and try
1. Setup
   1. Clone<br>
   ```shell
    git clone https://github.com/minientreprise-scv/is-a-plant-in-image-ai.git
    ```
   2. Make cli executable
   ```shell
    chmod +x cli
    ```

2. Download th GPT or train your own model
```shell
./cli download-gpt
```
This will download the GPT in models/GPT-yy-mm-dd
```shell
./cli train dataset-dir/
```
This will train and save a model in models/OWN-yy-mm-dd

3. Try with your own photos or with examples in `examples/`
```shell
./cli examples/flower.png [--model models/OWN-yy-mm-dd]
```


## Goals
-[ ] Detect plants and flowers
-[ ] Document the package
-[ ] Publish the package
-[ ] Release a GPT that is autodownload by package
-[ ] Cli to train and detect

## Credits

- This project uses `numpy`, `imageia`