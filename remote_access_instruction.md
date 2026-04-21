## Remote Usage (for Server Users)

To run this project on the server, each user must configure their own environment.

### 1. SSH into the server(or other ways)

```bash
ssh your_username@server_address
```

---

### 2. Configure AWS Credentials

Each user must set up credentials in their own home directory:

```bash
mkdir -p ~/.aws
nano ~/.aws/credentials
```

Add:

```
[default]
aws_access_key_id=YOUR_ACCESS_KEY
aws_secret_access_key=YOUR_SECRET_KEY
```

Set file permissions:

```bash
chmod 600 ~/.aws/credentials
```

---

### 3. Install Dependencies (if not already installed)

```bash
pip install -r requirements.txt
```

---

### 4. Run the Training Script

```bash
python training.py
```

---

### Notes

* Credentials are user-specific and not shared
* Do NOT commit credentials to the repository
* The same codebase is shared across users, but each user runs it with their own credentials
