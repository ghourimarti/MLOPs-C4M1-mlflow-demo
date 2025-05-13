# Listing environments
# To see a list of all your environments:
conda info --envs

# remove environment
conda env remove -n mlflow-env


# create environment
# To create a new environment, use the following command:
conda env create -f conda.yaml
conda activate mlflow-env


# 
# python main.py --learning_rate 0.01 --epochs 100
