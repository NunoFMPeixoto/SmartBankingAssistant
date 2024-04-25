import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


def replicate_gpt4(query):
    # Implementation for Replicate provider with GPT-4
    pass

def langchain_gpt4(query):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    # using gpt 3.5 for test usage due to pricing
    llm = ChatOpenAI(model_name="gpt-4-turbo", openai_api_key=openai_api_key)
    prompt = PromptTemplate(
        input_variables=["query"],
        template="""You are a banking assistant. Classify the user's intention based on the following query:

                    {query}

                    To determine the intention, consider the following:

                    - If the query contains words like "balance", "account", or mentions checking the balance, it likely indicates an intent to check the account balance.

                    - If the query mentions "transfer", "send money", or specifies an amount and recipient, it likely indicates an intent to make a money transfer.

                    - If the query contains words like "pay", "bill", "credit card", or mentions paying a specific bill, it likely indicates an intent to make a bill payment.

                    - If the query mentions "open", "new account", "savings account", or similar terms, it likely indicates an intent to open a new account.

                    - If the query asks about specific banking products, interest rates, or wants to compare products, it likely indicates an intent to inquire about products.

                    If the intention is still unclear, answer "unknown intention".

                    Answer with one possible intentions: account balance, money transfer, bill payment, account opening, product inquiry, unknown intention.
                """
    )
    intention = llm.invoke(prompt.format(concept="autoencoder", query=query))
    return intention.content.strip()