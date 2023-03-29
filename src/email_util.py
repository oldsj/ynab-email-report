from redmail import EmailSender

import os

def send_email(
        net_balance, 
        transactions, 
        chart,
        checking_balance,
        savings_balance,
        credit_card_balance
    ):
    recipients = os.getenv("MAIL_RECIPIENTS")
    recipients = recipients.split(",")
    sender = os.getenv("MAIL_USERNAME")
    subject = os.getenv("MAIL_SUBJECT")
    smtp_server = os.getenv("MAIL_SERVER")
    smtp_port = os.getenv("MAIL_PORT")
    username = os.getenv("MAIL_USERNAME")
    password = os.getenv("MAIL_PASSWORD")

    # Initialize the EmailSender instance
    email = EmailSender(
        host=smtp_server,
        port=smtp_port,
        username=username,
        password=password,
    )
    email.receivers = recipients
    email.set_template_paths(html="templates")

    # Send the email
    email.send(
        sender=f"{sender} <{username}>",
        subject=subject,
        html_template="report.html.j2",
        body_images={
            # "fi_plot": fig,
            "net_balance_chart": chart
        },
        body_params={
            # "time_to_fi": "1",
            "net_balance": net_balance,
            "transactions": transactions,
            "checking_balance": checking_balance,
            "savings_balance": savings_balance,
            "credit_card_balance": credit_card_balance,
        },
        # body_tables={
        #     "top_inflows": top_inflows,
        #     "top_outflows": top_outflows,
        #     "snapshot": snapshot
        # }
    )
