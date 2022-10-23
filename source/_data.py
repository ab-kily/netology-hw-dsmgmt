"""
This file will contain code related to the downloading or creation of data, if deemed necessary
"""
import kaggle
import pandas as pd
kaggle.api.authenticate()
kaggle.api.dataset_download_files('rajyellow46/wine-quality', path='../data/raw', unzip=True)

dataraw = pd.read_csv("../data/raw/winequalityN.csv")
