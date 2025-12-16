# Text Summarization Project

This project implements an end-to-end Text Summarization pipeline using the **Google Pegasus** model. It includes data ingestion, validation, transformation, model training, evaluation, and a prediction pipeline served via a **FastAPI** web application.

## Project Overview

Welcome to the **Text Summarization Project**! This application leverages the power of the **Google Pegasus** model to transform lengthy dialogue conversations into concise, meaningful summaries.

Whether you're looking to quickly understand chat logs or experiment with NLP pipelines, this project offers a robust, modular, and easy-to-deploy solution. It is built on the **SAMSum dataset** and strictly adheres to industry-standard MLOps practices.

### Key Features
- **Modular Pipeline**: Broken down into stages (Ingestion, Validation, Transformation, Training, Evaluation).
- **FastAPI Application**: A web interface and API for real-time text summarization.
- **Docker Support**: Containerized for easy deployment.
- **CI/CD Integration**: Includes GitHub Actions workflows.

## Workflows

1.  **Update `config.yaml`**: Define paths and configuration for each stage.
2.  **Update `params.yaml`**: Set model training parameters (epochs, batch size, etc.).
3.  **Update Entity**: Define data classes for configuration verification.
4.  **Update Configuration Manager**: Map config files to entity classes.
5.  **Update Components**: Implement the logic for each stage.
6.  **Update Pipeline**: Orchestrate the components.
7.  **Update `main.py`**: Entry point for running the training pipeline.
8.  **Update `app.py`**: Entry point for the web application.

## How to Run

### Local Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Subamprasad/Text-Summarizer.git
    cd Text-Summarizer
    ```

2.  **Create a virtual environment**:
    ```bash
    conda create -n summary python=3.8 -y
    conda activate summary
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Training Pipeline**:
    ```bash
    python main.py
    ```
    *Note: This will download data, train the model (or use pre-trained), and evaluate it.*

5.  **Run the Web Application**:
    ```bash
    python app.py
    ```
    Open your browser at `http://localhost:8081`.

### Docker

1.  **Build the image**:
    ```bash
    docker build -t text-summarizer .
    ```

2.  **Run the container**:
    ```bash
    docker run -p 8081:8081 text-summarizer
    ```

## API Documentation

The application exposes the following endpoints:

-   `GET /`: Serves the web interface.
-   `POST /predict`: Accepts JSON payload `{"text": "your dialogue here"}` and returns the summary.
-   `GET /train`: Triggers the training pipeline (requires authentication or local execution).

## Usage Note

> [!NOTE]
> **Prediction Latency**: When converting "Text to Summarize" to a "Summary", please be patient. It will take a little bit of time to summarize the text as the model processes the input.

## Directory Structure
- `src/textSummarizer`: Main source code.
- `research/`: Jupyter notebooks for experimentation.
- `config/`: Configuration files.
- `artifacts/`: Generated files (data, models, metrics) - *Excluded from git*.

## Author
Subam Prasad
