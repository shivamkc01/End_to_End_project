#!/bin/bash --login

# Entire script fails if a single command fails
set -e

cd ..
PROJECT_DIR="$PWD/End_to_End_data_science_project_advance"

ENV_PREFIX="$PROJECT_DIR/env"
# Source Conda initialization script
echo $PROJECT_DIR
source ~/anaconda3/etc/profile.d/conda.sh

conda env create --prefix "$ENV_PREFIX" --file "$PROJECT_DIR/environment.yml" --force
