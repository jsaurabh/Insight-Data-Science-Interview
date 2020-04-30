#!/bin/bash

[ -d data ] || mkdir data
cd data

#Download movies data from Kaggle
kaggle datasets download -d tmdb/tmdb-movie-metadata
echo "Data downloaded successfully"

unzip tmdb-movie-metadata.zip
echo "Data unzipped at location $PWD"

rm tmdb-movie-metadata.zip