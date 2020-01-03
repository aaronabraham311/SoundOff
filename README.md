# SoundOff
In this project, I wanted to investigate whether audio sound patterns has significantly differed in music from the 70s, 80's, 90s, 00's and the 2010s. Ultimately, I created a quick model that can classify songs from different decades solely based on audio patterns with an accuracy of 67%.

Originally, I wanted to create a model that can distinguish music based on year (2010 vs. 2011 .... vs. 2018). Unfortunately, I was not able to scrape much data and found inconclusive results (ex: classification model had an accuracy of 15%).

I also wanted to scrape music from Soundcloud to create a small service for amateur artists to predict their song's popularity, but the Soundcloud API was unfortunately deprecated.

## Steps:
1. Scraped Youtube playlists that contained 100+ songs from each decade using youtube-dl
    * Script can be found in `scripts/youtube_download.py`
2. Performed preprocessing: Created a dataset with several audio features for each song (chroma STFT, tempo, spectral features, etc.)
    * Script for decade-by-decade preprocessing can be found in `scripts/preprocessing.ipynb`
    * Processed dataset (year-by-year) can be found in `data/processed_data.csv`
    * Processed dataset (decade-by-decade, one used in this project) can be found in `data/revamped_processed_data.csv`
3. Exploratory data analysis: I created numerous visuals to uncover audio patterns, including boxplot, 3D scatter plots and t-SNE plots. The goal for this project was to learn as many new statistical tricks that I can. In those efforts, I used the following statistical analysis tools to uncover key patterns:
    * Regression testing
    * ANOVA and Tukey analysis
    * Principal component analysis
    * Script for year-by-year EDA: `scripts/eda.ipynb`
    * Script for decade-by-decade EDA: `scripts/eda_new_version.ipynb`
4. Machine learning: The newest skill that I tried to incorporate was Bayesian optimization using the `hyperopt` package. Furthermore, I created a simple logistic regression model and analyzed odd ratios and other statistics.
    * Script for year-by-year ML: `scripts/ml.ipynb`
    * Script for decade-by-deaced Ml: `scripts/ml_new_version.ipynb`

## Replication:
1. Clone this repository and `cd` to it
2. Create a virtual environment
3. Type `pip install -r requirements.txt`

## Sample Images: 
![Heatmap](https://user-images.githubusercontent.com/21224282/71741813-0d486900-2e1d-11ea-976e-f51b89837cc8.png)
![PCA](https://user-images.githubusercontent.com/21224282/71741925-5ef0f380-2e1d-11ea-9cce-dbc8cacd131d.png)
![t-SNE](https://user-images.githubusercontent.com/21224282/71741953-762fe100-2e1d-11ea-8096-f4ec52fb5c63.png)

## Future steps: 
I aim to do the following in this project
1. Create my own song using GAN 
    * No idea how I will achieve this but will do more research
2. Create service that artists can use to predict their song popularity
    * Need to create a Flask app that takes an MP3 and ports it into cloud
    * Run machine learning code in the cloud to pre-process music
    * Output predictions but in visually appealing way 
