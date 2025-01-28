from flask import Flask, request, render_template, Response
import joblib
import os
from dotenv import load_dotenv
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

# Email credentials
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")
to_email = os.getenv("EMAIL_USER")  # Replace with alert recipient if different

def send_alert_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        text = msg.as_string()
        server.sendmail(email_user, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

app = Flask(__name__)

model = joblib.load("trained_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        query = request.form["query"]
        X = vectorizer.transform([query])
        prediction = "Malicious" if model.predict(X)[0] == 1 else "Safe"
        if prediction == "Malicious":
            send_alert_email("SQL Injection Alert", f"Query: {query}\nURL: {request.url}")
    return render_template("index.html", prediction=prediction)

@app.route("/validate", methods=["POST"])
def validate():
    query = request.form["query"]
    X = vectorizer.transform([query])
    prediction = model.predict(X)[0]
    if prediction == 1:
        send_alert_email("Cross-Site Scripting Alert", f"Query: {query}\nURL: {request.url}")
        return Response("Malicious content detected.", status=403)
    return Response("Content is safe.", status=200)

@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    if request.method == 'POST':
        query = request.form.to_dict()
        query_string = '&'.join([f'{key}={value}' for key, value in query.items()])
        X = vectorizer.transform([query_string])
        prediction = model.predict(X)[0]
        if prediction == 1:
            send_alert_email("Malicious Request Alert", f"Query: {query_string}\nURL: {request.url}")
            return Response("The request has been blocked by the WAF.", status=403)
    return Response("Proxy route accessed successfully.", status=200)

if __name__ == "__main__":
    app.run(port=5000)
