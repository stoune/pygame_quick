# PyGame basic tutorial

Based on [PyGame Zero introduction tutorial](https://pygame-zero.readthedocs.io/en/stable/introduction.html).

# Env setup

## Conda preparation

```shell
conda update conda

conda env create -f environment.yml --prefix ./.env
conda activate ./.env

## Remove env
# conda deactivate && conda env remove -n pygame
## Export conda env
# conda env export > environment.yml
# conda activate pygame
# pip install -r requirements.txt
## install pip in the env 
# conda install -n pygame pip
# To deactivate an active environment, use
#
#     $ conda deactivate

# updating your env 
# conda env update --prefix ./.env --file environment.yml  --prune

# Read more https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

## Setting environment variables

conda env config vars list
conda env config vars set TEST_VAR=value

# Exporting environment.yml
conda env export > environment.yml

# Open folder in VS Code 
code .

```

# Resources

[Platformer Art Deluxe](https://kenney.nl/assets/platformer-art-deluxe)

```
# Mac or Linux instruction
# depends on presence of curl and jar
cd src
chmod +x ./download_res.sh
./download_res.sh 
```
