# NoGas_IDO
Projet - Développement d'application IDO

## Prerequisites
- Python 3.12
- Raspberry Pi

## Getting started
1. Create a python venv
```bash
cd NoGas_IDO
python3 -m venv .
```
2. Install dependencies from requirements.txt
```bash
bin/pip install -r requirements.txt
```

3. Launch script
```bash
bin/python3 nogas.py
```
### Example env file 
user must be admin 
CRED={"email":"nogas@gmail.com","password":"gas-123"}
LOGIN_URL="http://10.10.23.172:3001/user/login"
ADD_DATA_URL="http://10.10.23.172:3001/addData"
