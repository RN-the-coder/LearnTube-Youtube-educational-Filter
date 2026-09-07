# LearnTube

LearnTube is a full-stack web application that helps users find educational YouTube videos while reducing distractions.

The application searches YouTube through the YouTube Data API, evaluates each video's title with a machine learning classifier, filters out videos that are unlikely to be educational, and ranks the remaining results by educational probability.

## Features

- Search YouTube videos from a clean, distraction-free interface
- Filter results using a machine learning model
- Rank educational videos by classification probability
- Watch videos inside LearnTube using the YouTube embedded player
- Minimal responsive React interface
- Django REST API backend
- YouTube Data API v3 integration
- Environment-variable based configuration

## Tech Stack

### Frontend
- React
- Vite
- React Router
- JavaScript
- CSS

### Backend
- Python
- Django
- Django REST Framework
- django-cors-headers

### Machine Learning
- scikit-learn
- TF-IDF
- Logistic Regression
- pandas
- joblib

### External API
- YouTube Data API v3

## How It Works

```text
User search
    ↓
React frontend
    ↓
Django REST API
    ↓
YouTube Data API
    ↓
YouTube video titles
    ↓
TF-IDF vectorization
    ↓
Logistic Regression
    ↓
Educational probability
    ↓
Decision threshold
    ↓
Filter + rank results
    ↓
React frontend
```

LearnTube currently classifies videos using their titles.

The classifier returns a probability representing how likely a title is to belong to educational content. Videos below the selected decision threshold are removed, and the remaining videos are sorted by educational score.

## Machine Learning Model

The final dataset contains 394 manually reviewed YouTube video titles:

- 199 educational
- 195 non-educational

The dataset was divided into training and test sets using an 80/20 split with stratification.

Text features are generated using TF-IDF with unigrams and bigrams:

```python
TfidfVectorizer(
    ngram_range=(1, 2),
    lowercase=True,
    strip_accents="unicode"
)
```

The resulting vectors are classified using Logistic Regression.

### Evaluation

At a decision threshold of `0.55`, the model achieved the following results on the held-out test set:

| Metric | Result |
| --- | ---: |
| Accuracy | 96.20% |
| Precision | 100.00% |
| Recall | 92.50% |
| F1 Score | 96.10% |

Confusion matrix:

```text
[[39  0]
 [ 3 37]]
```

The higher threshold was selected to prioritize precision over recall. For LearnTube, allowing fewer non-educational videos into the results is more important than recovering every possible educational video.

> These metrics describe performance on the project's held-out test set and do not imply the same accuracy across all YouTube videos.

## Project Structure

```text
LearnTube/
├── Frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.jsx
│   │   │   └── VideoResult.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── SearchResults.jsx
│   │   │   └── Watch.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── .env.example
│   └── package.json
│
└── Backend/
    ├── config/
    ├── videos/
    │   ├── services/
    │   │   ├── classifier.py
    │   │   └── youtube.py
    │   ├── urls.py
    │   └── views.py
    ├── ml/
    │   ├── educational_model.joblib
    │   ├── real_titles_training.csv
    │   └── train_model.py
    ├── manage.py
    └── .env.example
```

## Local Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd LearnTube
```

### 2. Backend

```bash
cd Backend
python -m venv venv
```

Activate on Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
YOUTUBE_API_KEY=your_youtube_api_key
```

Run Django:

```bash
python manage.py runserver
```

The backend runs at:

```text
http://127.0.0.1:8000
```

### 3. Frontend

Open another terminal:

```bash
cd Frontend
npm install
```

Create a `.env` file:

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

Start Vite:

```bash
npm run dev
```

Open the URL displayed by Vite, usually:

```text
http://localhost:5173
```

## Retraining the Model

From the `Backend` directory:

```bash
python ml/train_model.py
```

The script:

1. Loads the manually labeled title dataset
2. Creates an 80/20 train-test split
3. Fits the TF-IDF vectorizer on the training data
4. Trains Logistic Regression
5. Evaluates classification performance
6. Saves the trained model to `ml/educational_model.joblib`

## Environment Variables

### Backend

```env
YOUTUBE_API_KEY=your_youtube_api_key
```

### Frontend

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

Do not commit real `.env` files or API keys.

## Current Limitations

- Classification is based only on video titles.
- Ambiguous titles may be misclassified.
- The training dataset is relatively small.
- YouTube search results depend on the YouTube Data API.
- Educational quality is treated as a binary classification problem rather than a detailed quality assessment.

Possible future improvements include:

- Larger and more diverse labeled datasets
- Additional metadata features
- More advanced NLP models
- User accounts and saved videos
- Search history and favorites
- Model monitoring and periodic retraining

## Why This Project

LearnTube was built as a practical full-stack and machine learning project combining:

- frontend development
- REST API design
- third-party API integration
- supervised machine learning
- NLP feature extraction
- model evaluation
- product-oriented decision threshold tuning

The project demonstrates how a machine learning model can be integrated into a real web application instead of existing only as an isolated notebook or experiment.

## License

This project is intended for educational and portfolio purposes.
