import base64
from io import BytesIO
import matplotlib.pyplot as plt
import mplcyberpunk
from datetime import date
from datetime import datetime, timedelta
from email.mime.image import MIMEImage
from db import fetch_net_balance_data

def generate_chart(net_balance_today):
    # Create a sample net balance data for the past month (replace with real data)
    days = 30
    dates = [date.today() - timedelta(days=i) for i in range(days)]
    # net_balances = fetch_net_balance_data(days)
    net_balances = [net_balance_today - i * 1000 for i in range(30)]

    # Create the graph using matplotlib and mplcyberpunk
    fig = plt.figure()
    plt.style.use("cyberpunk")
    plt.plot(dates, net_balances)
    plt.xlabel("Date")
    plt.ylabel("Net Balance")
    plt.title("Liquid Savings")
    mplcyberpunk.add_glow_effects()

    chart = fig

    return chart
