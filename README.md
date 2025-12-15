# Physician Notetaker – Medical NLP System

## Overview
This project demonstrates an AI-based Physician Notetaker system that processes
doctor–patient conversations and extracts structured medical information using
Natural Language Processing (NLP).

The system converts unstructured medical transcripts into:
1) Structured medical summaries
2) Patient sentiment and intent analysis
3) SOAP (Subjective, Objective, Assessment, Plan) notes

This project is designed for educational and demonstration purposes only.

---

## Features
1) Medical entity extraction (Symptoms, Diagnosis, Treatment, Prognosis)
2) Keyword extraction from clinical text
3) Patient sentiment classification (Anxious, Neutral, Reassured)
4) Patient intent detection (Reporting symptoms, Seeking reassurance, Expressing relief)
5) Automated SOAP note generation

---

## Project Structure
Physician-Notetaker/
│
├── physician_notetaker.ipynb # Jupyter Notebook with code and outputs
├── physician_notetaker.py # Python script version
├── requirements.txt # Required Python libraries
└── README.md # Setup and usage instructions

---

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- pip package manager
- Jupyter Notebook

---

### 2. Install Dependencies
Run the following command in the project directory:

```bash
pip install -r requirements.txt

#To run Jupyter Notebook - jupyter notebook physician_notetaker.ipynb
#To run python script - python physician_notetaker.py

