# Automated Weekly Email Sender using GitHub Actions

This project enables automated weekly emails to be sent from a personal Gmail account using GitHub Actions. The email content and recipient list are predefined in the `app.py` file. This system does not require a server or manual execution — it runs entirely through GitHub’s CI infrastructure.

---

## 🚀 Features

- Sends an email every Monday at 8:30 AM IST
- Uses Python and Gmail SMTP
- Fully automated with GitHub Actions
- No manual deployment required
- Secrets are safely stored using GitHub Actions Secrets

---

## 🔧 Configuration Steps

### 1. Gmail Setup: Generate an App Password

To allow GitHub Actions to send emails from your Gmail account, you must generate an App Password.

1. Go to: https://myaccount.google.com/apppasswords  
2. Enable **2-Step Verification** if you haven’t already  
3. Select "Mail" as the app and "Other" or "GitHub" as the device  
4. Click **Generate** and copy the 16-character App Password  
5. Note: Use this App Password in place of your actual Gmail password

---

### 2. Set Repository Secrets on GitHub

Go to your GitHub repository → `Settings` → `Secrets and variables` → `Actions` → `New repository secret`.

Add the following:

| Secret Name | Value                         |
|-------------|-------------------------------|
| `EMAIL`     | Your Gmail address            |
| `PASSWORD`  | The 16-character App Password |

---

### 3. Verify Files in Repository

Ensure the following files are present:

#### ✅ `app.py`

Contains the logic for sending the email using `smtplib`.

#### ✅ `.github/workflows/send_email.yml`

Contains the GitHub Actions workflow that runs `app.py` every Monday.

---

## 📅 How It Works

- **Trigger**: The GitHub Actions workflow is triggered every Monday at 3:00 AM UTC (8:30 AM IST) using a cron schedule.
- **Job**: It sets up Python, injects the email credentials using secrets, and runs `app.py`.
- **Result**: An email is sent to the configured recipients.

---

## ✅ Manual Test (Optional)

To test immediately:

1. Go to the `Actions` tab of your GitHub repo  
2. Select the workflow named "Weekly Email Automation"  
3. Click **"Run workflow"**

---

## 📬 Customize

You can modify the following inside `app.py`:

- **Recipients**: Add/remove emails in the `recipients` list  
- **Subject and Body**: Change the contents of the email as per your needs

---
