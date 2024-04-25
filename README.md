# SmartBankingAssistant

📝 Imagine you're on a banking website, and you want to implement an intention classifier. When a customer writes a sentence, your goal is to classify it into one of the following categories:

| Sentence                                 | Classification     |
|------------------------------------------|-------------------|
| Check my balance                         | account balance   |
| Transfer $500 to John                    | money transfer    |
| Pay my credit card bill                  | bill payment      |
| Open a new savings account               | account opening   |
| What is the interest rate for loans?     | product inquiry   |
| I love the movie "The Shawshank Redemption" | unknown intention |

In this exercise, we have only 5 possible intentions:
- account balance
- money transfer
- bill payment
- account opening
- product inquiry

However, there could also be a 6th category: "unknown intention".

The ultimate goal is to create a process that, given a sentence, classifies it into one of the 6 intentions.

## 🚀 Getting Started

To get started with SmartBankingAssistant, follow these steps:

1. Clone the repository:
```bash
  git clone https://github.com/your-username/SmartBankingAssistant.git
```

2. Navigate to the project directory:
```bash
  cd SmartBankingAssistant
```

3. Create a virtual environment (recommended):
```bash
  python -m venv .venv
```

4. Activate the virtual environment:
- For Windows:
```bash
  .venv\Scripts\activate
```
- For macOS and Linux:
```bash
  source .venv/bin/activate
```

5. Install the required dependencies:
```bash
  pip install -r requirements.txt
```

6. Create a .env file in the project root directory and add your OpenAI API key::
```bash
  OPENAI_API_KEY=your_open_ai_key
```


## 🏃‍♂️ Running the Classifier

To run the Prozis Intention Classifier:
```bash
  python main.py
```

This command will start the FastAPI server, and you can access the API endpoints to classify customer sentences.

## 🖥️ Running the Frontend

To run the SmartBankingAssistant Intention Classifier frontend using Streamlit:

1. Make sure you have the backend server running. Open a terminal and navigate to the project directory, then run:

```bash
   python main.py
```

   This will start the FastAPI server.

3. Run the following command to start the Streamlit frontend:

```bash
   streamlit run frontend_app.py
```

   This will launch the Streamlit application in your default web browser.

Now you have the backend server running and the frontend accessible through Streamlit. You can interact with the Prozis Intention Classifier using the Streamlit UI.

## 📡 API Endpoints

The Prozis Intention Classifier provides the following API endpoint:

- **POST /v1/classify:** Classifies a customer sentence into one of the 6 intentions. 

  **Request Body:**
  ```json
  {
      "phrase": "your_customer_sentence",
      "model": "model_name",
      "provider": "provider_name",
      "similarity_search_method": "search_method"
  }

- **phrase:** The customer sentence to classify.
- **model:** The name of the model to use for classification (e.g., "gpt4").
- **provider:** The provider of the model (e.g., "langchain").
- **similarity_search_method:** The similarity search method to use (e.g., "sentence_transformer").


  **Response:**
  ```json
  {
    "intention": "classified_intention"
  }

## 🌟 Features

- Modular architecture for easy extensibility and maintainability.
- Support for multiple models and providers for intention classification.
- Configurable similarity search methods for improved accuracy.
- Easy integration with the Prozis website.


