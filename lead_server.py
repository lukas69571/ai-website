from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from pathlib import Path
import json
import csv
from datetime import datetime
import smtplib
from email.message import EmailMessage
import requests

BASE = Path('leads')
CSV_FILE = BASE / 'leads.csv'
JSON_FILE = BASE / 'leads.json'

SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'dein@email.com'
SMTP_PASS = 'PASSWORT'
EMAIL_TARGET = 'sales@deinefirma.de'

CRM_API_URL = 'https://api.mailerlite.com/api/v2/subscribers'
CRM_API_KEY = 'DEIN_API_KEY'

def send_email_notification(lead):
    from email.message import EmailMessage
    msg = EmailMessage()
    msg['Subject'] = f"Neuer Lead: {lead['name']}"
    msg['From'] = SMTP_USER
    msg['To'] = EMAIL_TARGET
    msg.set_content(f"Neuer Lead:\\nName: {lead['name']}\\nEmail: {lead['email']}\\nSeite: {lead['source_page']}\\nZeit: {lead['received_at']}")
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)

def push_to_crm(lead):
    headers = {"Content-Type": "application/json", "X-MailerLite-ApiKey": CRM_API_KEY}
    data = {"email": lead["email"], "name": lead["name"], "fields": {"source_page": lead["source_page"]}}
    response = requests.post(CRM_API_URL, headers=headers, json=data)
    return response.status_code

def process_new_lead(lead):
    file_exists = CSV_FILE.exists()
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=lead.keys())
        if not file_exists: writer.writeheader()
        writer.writerow(lead)

    leads = []
    if JSON_FILE.exists():
        leads = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    leads.append(lead)
    JSON_FILE.write_text(json.dumps(leads, indent=2), encoding="utf-8")

    try: send_email_notification(lead); print(f"✅ E-Mail an {EMAIL_TARGET} gesendet.")
    except Exception as e: print(f"⚠️ E-Mail Versand fehlgeschlagen: {e}")
    try:
        status = push_to_crm(lead)
        if status in [200, 201]: print(f"✅ Lead {lead['email']} an CRM gesendet.")
        else: print(f"⚠️ CRM Push fehlgeschlagen: Status {status}")
    except Exception as e: print(f"⚠️ CRM Push Exception: {e}")

class LeadHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/lead":
            self.send_response(404); self.end_headers(); return
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode()
        data = {k: v[0] for k, v in parse_qs(body).items()}
        data["received_at"] = datetime.utcnow().isoformat()
        process_new_lead(data)
        self.send_response(302); self.send_header("Location", "/danke"); self.end_headers()

if __name__ == "__main__":
    print("🚀 Lead Server läuft auf http://localhost:8000")
    HTTPServer(("localhost", 8000), LeadHandler).serve_forever()
