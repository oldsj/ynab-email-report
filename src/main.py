from email_util import send_email
from report import generate_chart
from ynab import get_net_balance, get_yesterday_transactions, get_account_balances

yesterday_transactions = get_yesterday_transactions()
account_balances = get_account_balances()
checking_balance = account_balances["checking"]/1000
savings_balance = account_balances["savings"]/1000
credit_card_balance = account_balances["credit_card"]/1000
net_balance_today = get_net_balance(checking_balance, savings_balance, credit_card_balance)

# Generate the HTML content and inline image
chart = generate_chart(net_balance_today)

# Send the email
send_email(
    net_balance_today,
    yesterday_transactions,
    chart,
    checking_balance,
    savings_balance,
    credit_card_balance,
    )
