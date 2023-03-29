import datetime
import requests
import requests_cache
import os

requests_cache.install_cache(".cache/ynab_cache", expire_after=3600)  # Cache expires after an hour
base_url = "https://api.youneedabudget.com/v1"
api_key = os.getenv("YNAB_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}

# Get your budget ID
response = requests.get(f"{base_url}/budgets", headers=headers)
budgets = response.json()["data"]["budgets"]
budget_id = budgets[0]["id"]

# Get budget details
response = requests.get(f"{base_url}/budgets/{budget_id}", headers=headers)
budget_detail = response.json()["data"]["budget"]


# Get accounts and balances
accounts = budget_detail['accounts']

def get_yesterday_transactions():
    # Get the previous day's transactions
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    response = requests.get(f"{base_url}/budgets/{budget_id}/transactions", headers=headers, params={"since_date": yesterday})
    transactions = response.json()["data"]["transactions"]

    # Filter transactions (excluding transfers)
    filtered_transactions = [t for t in transactions if t['transfer_transaction_id'] is None]

    return filtered_transactions

def get_account_balances():
    # Calculate current balances
    credit_card_balance = sum([-a['balance'] for a in accounts if a['type'] == 'creditCard' and a['name'] != 'Optum HSA'])
    checking_balance = sum([a['balance'] for a in accounts if a['type'] == 'checking' and a['name'] != 'Optum HSA'])
    savings_balance = sum([a['balance'] for a in accounts if a['type'] == 'savings'])

    return {
        "credit_card": credit_card_balance,
        "checking": checking_balance,
        "savings": savings_balance,
    }

def get_net_balance(checking_balance, savings_balance, credit_card_balance):
    # Calculate the net balance of cash minus debt from credit cards
    return (checking_balance + savings_balance) - credit_card_balance

