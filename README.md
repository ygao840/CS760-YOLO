1. `label.py` is used to generate the distribution plot of the labels in datasets\
2. `main.py` is used to train the model, you need to specify the pretrained model and network's yaml file's path, you also need to set the hyperparameter and dataset's yaml file's path in`model.train()`. Make sure you have already install the `ultralytics` package\
3. `read_results` is used to read `results.csv` in `runs/detect`. All you need is to custome the path and legend names.\
4. If you want to use COMET ML to tracking and compare the models, plz put your token into `Comet.py`. Before run the code, make sure you have already install the `comet_ml` package.\
`Subset.py` is used to generate a subset with a certain number of samples. You need to specify the input and output paths, also the number of samples in the subset.\
Becareful:\

No actual dataset and output model(`best.pt` and `last.pt`) is provided.\
- Dataset: You can download the dataset according to the link in the `data.yaml` in each dataset folder.\
- Output model: I cannot provide the model because of the GitHub upload limitation, only val plots and `results.csv` is provided. If you want the model, plz contact me.\ 
