# Automated MLOps Pipeline for Continuous Learning

This repository demonstrates an automated MLOps pipeline for continuous model retraining and learning. It detects data drift, retrains models, and publishes the model to github container registry using GitHub Actions.

<img src="https://i.redd.it/50yslv18hse71.jpg" style="width: 300px;" alt="meme">

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/SubhasmitaSw/automated-model-retraining-demo.git
   cd automated-model-retraining-demo 
   ```

2. Set up a virtual environment:
   ```
   python3 -m venv .venv && source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Train the initial model:
   ```
   python src/main.py
   ```

2. To simulate data drift instill a change in data or modify the drift percentage and retrain the model:
   ```
   python retraining/retrain.py
   ```

3. To run the API locally:
   ```
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

4. Test the if the model is listening via the API by running the `api_test.ipynb`

5. To run the Docker container, download the package, then:
   
   ```
   docker run -p 8000:8000 automated-model-retraining-demo 
   ```

## GitHub Actions Pipeline

This repository uses a GitHub Actions workflow for continuous integration and deployment.

The pipeline performs the following steps:

1. Sets up the Python environment
2. Installs dependencies
3. Runs the retraining script to check for drift and retrain if necessary
4. If the model was retrained, commits and pushes the new model
5. Builds a Docker image containing the latest code and model
6. Pushes the Docker image to GitHub Container Registry

To use the GitHub Actions pipeline:

1. Ensure your repository has GitHub Packages enabled
2. The workflow will run automatically on the specified triggers
3. You can manually trigger the workflow from the "Actions" tab in your GitHub repository
4. Make sure to add your GITHUB_TOKEN to the repository
