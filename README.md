# Crypto_price_prediction
Cryptocurrency Price Prediction using Deep Learning and AI

Description:

This project aims to predict the prices of cryptocurrencies using machine learning techniques, including deep learning models like LSTM, BiLSTM, CNN-LSTM, and Transformers. The project integrates real-time market data to forecast the prices of cryptocurrencies based on historical data and various technical indicators (RSI, MACD, Bollinger Bands).

The project is built using a combination of Python, TensorFlow, and FastAPI for backend development, with React.js and TypeScript for frontend development. It includes a real-time price prediction dashboard where users can interact with the model to get price forecasts.

Features:
	•	Real-time Cryptocurrency Prediction: Get price predictions for multiple cryptocurrencies.
	•	Deep Learning Models: Integration of LSTM, BiLSTM, CNN-LSTM, and Transformer-based models for enhanced accuracy.
	•	Technical Indicators: Includes RSI, MACD, and Bollinger Bands for feature engineering.
	•	Real-time Market Data Integration: Continuous data updates for cryptocurrency prices using API integrations.
	•	Web Dashboard: An interactive UI built using React.js and Redux to display predictions and data.
	•	Backend API: FastAPI backend handling data fetching, predictions, and real-time updates.
	•	Deployment: Deployed as a web application using Docker and Heroku.
	•	ONNX/TensorFlow Lite Support: Convert models for mobile/edge deployment.
	•	Step-by-Step Documentation: A detailed guide for setting up and running the project.

What’s Included:
	Notebooks:
	•	data_exploration.ipynb: Data analysis and visualization.
	•	model_training.ipynb: Model training and experiments.
	Scripts:
	•	evaluate.py: Evaluating the model performance.
	•	preprocess.py: Data preprocessing for model input.
	•	train_model.py: Script for training the models.
	Models:
	•	Pre-trained models such as lstm_model.h5, bilstm_model.h5, cnn_lstm_model.h5, attention_model.h5.
	Web App:
	•	app.py: Main FastAPI app to handle predictions.
	•	predict.py: Logic for processing user input and generating predictions.
	Frontend:
	•	Web UI built using React.js, Redux, and TypeScript for displaying predictions.
	Deployment:
	•	Docker configurations for easy deployment.
	•	Heroku deployment guide for hosting the web app.
	Other:
	•	requirements.txt: Python dependencies.
	•	README.md: Documentation to guide you through setting up the project.
	•	.gitignore: For ignoring unnecessary files in the repo.

 git clone https://github.com/yourusername/cryptocurrency-price-prediction.git
 
cd cryptocurrency-price-prediction

pip install -r requirements.txt
