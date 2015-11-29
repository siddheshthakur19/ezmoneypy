import requests
import json

AUTH='Bearer X6oCsq_W4w1mUnwRSepY3nrS6bQa'
APP_ID='SmartPayAndroid'
BASE_PATH = 'https://api.sit.modjadji.org:8243/TipsGo/v1.0.0/'
header = {'InstallationID':'5owEHoDDU0957kCSDLfWNqMzA8ZvcQSs', "Authorization":AUTH, "DeviceId":'SIM111112266666', "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
user_json = {'DateOfBirth': '04/04/1994', 'DisplayName': 'Hh','Email': 'fsdhasdaf@gj.co','FirstName': 'G','Gender': 'Male','PushID': 'd0EvfsWlVgA:APA91bHuZAJEQCVep6xtwSwhtY7G6qzMCWOb7OjjnyIOPnw4QpzfbqsN1o06GCc8bGIAE8D99bD2MvXJLZJ-4W8dUvuVE_1UbB1E6bs6ikc-V4JTyD_t9HvWyMO8-mpRwRxnDxorqR1u','Surname': 'B','WalletType': 'consumer'}

# Registers a new member -----------
def register_new_member(user_json):
    phone = user_json.pop('PhoneNo')
    device_id = user_json.pop('DeviceID')
    device_id = 'SIM111112266666'
    url = BASE_PATH + 'api/Wallet/RegisterWallet'
    header = {"Authorization":AUTH, "DeviceId":device_id, "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, data=json.dumps(user_json), headers=header).json()
    if response['Status'] == "000":
        user_json['InstallationID'] = response['DataObject']['InstallationID']
        user_json['DeviceID'] = device_id
        user_json['PhoneNo'] = phone
        return response['DataObject']['InstallationID'], 201
    else:
        return None, response['Status']


# Creates a new wallet ---------------
def create_wallet(create_json):
    device_id = create_json.pop('DeviceID')
    InstallationID = create_json.pop('InstallationID')
    url = BASE_PATH + 'api/Wallet/CreateWallet'
    header = {'InstallationID':InstallationID, "Authorization":AUTH, "DeviceId":device_id, "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, data=json.dumps(create_json), headers=header).json()
    if response['Status'] == "000":
        wallet_code = response['DataObject']['WalletCode']
        return wallet_code, 201
    return response['Status']

# Get wallet information
def get_wallet_info(wallet_json):
    device_id = wallet_json.pop('DeviceID')
    InstallationID = wallet_json.pop('InstallationID')
    wallet_code = wallet_json.pop('WalletCode')
    url = BASE_PATH + 'api/Wallet/GetWalletInfo?walletCode={}'.format(wallet_code)
    header = {'InstallationID':InstallationID, "Authorization":AUTH, "DeviceId":device_id, "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
    response = requests.get(url, headers=header).json()
    if response['Status'] == "000":
        wallet_info = response['DataObject'] # Info JSON
    else:
        wallet_info = None
    return wallet_info, response['Status']


# Get wallet list --------------------------
def get_wallet_list(list_json):
    pg_size = 0
    pg_num = 0
    InstallationID = list_json.pop('InstallationID')
    device_id = list_json.pop('DeviceID')
    url = BASE_PATH + 'api/Wallet/GetWalletList?pageSize={}&pageNum={}'.format(pg_size,pg_num)
    header = {'InstallationID':InstallationID, "Authorization":AUTH, "DeviceId":device_id, "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
    response = requests.get(url, headers=header).json()
    if response['Status'] == "000":
        wallet_list = response['ListOfObjects'] # List of dicts
    else:
        wallet_list = None
    return wallet_list, response['Status']



# Topup wallet --------------------------------
def top_up(topup_json):
    url = BASE_PATH + 'api/Wallet/TopUpWallet?walletCode={0}&date={1}&amount={2}&reason={3}'.format(topup_json['WalletCode'], topup_json['Date'], topup_json['Amount'], topup_json['Reason'])
    InstallationID = topup_json.pop('InstallationID')
    device_id = topup_json.pop('DeviceID')
    header = {'InstallationID':InstallationID, "Authorization":AUTH, "DeviceId":device_id, "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
    response = requests.get(url, headers=header).json()
    return response['Status']


# Merchant calls for payment. Exclusive for merchant side -----------------------------
def merchant_req_pay(bill_json):
    url = BASE_PATH + 'api/Wallet/InitPayment'
    InstallationID = bill_json.pop('InstallationID')
    device_id = bill_json.pop('DeviceID')
    header = {'InstallationID':InstallationID, "Authorization":AUTH, "DeviceId":device_id, "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
    bill_json= {"WalletCode":'4778207230271121553', "Amount":'2341', "Description":'sdfsdfa'}
    response = requests.post(url, headers=header, data=json.dumps(bill_json)).json() # Returns a Payment token -- auto sent to consumer device
    return response['Status']


# Customer confirms payment. Exclusive -----------
def confirm_payment(confirm_json):
    url = BASE_PATH + 'api/Wallet/ConfirmPayment'
    InstallationID = confirm_json.pop('InstallationID')
    device_id = confirm_json.pop('DeviceID')
    header = {'InstallationID':InstallationID, "Authorization":AUTH, "DeviceId":device_id, "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
    confirm_json = {"PaymentToken":'D/rApoJbQpC6Sf9XlCvughcBqMrGfv7O', "PIN":'123456'}
    response = requests.post(url,data=json.dumps(confirm_json),headers=header).json()
    return response['Status']


# TransferWallet
def transfer_between_wallets (transfer_json):
    InstallationID = transfer_json.pop('InstallationID')
    device_id = transfer_json.pop('DeviceID')
    url = BASE_PATH + 'api/wallet/TransferWallet?fromWalletCode={0}&toWalletCode={1}&date={3}&amount={2}&reason={4}'.format(transfer_json['SrcWallet'],transfer_json['DestWallet'],transfer_json['Amount'],transfer_json['Date'],transfer_json['Reason'])
    header = {'InstallationID':InstallationID, "Authorization":AUTH, "DeviceId":device_id, "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
    response = requests.get(url, headers=header).json()
    return response['Status']

def get_transaction_history(history_json):
    InstallationID = history_json.pop('InstallationID')
    device_id = history_json.pop('DeviceID')
    url = BASE_PATH+'api/wallet/GetWalletTransactions?walletCode={0}&startDate={1}&endDate={2}&pageSize=0&pageNum=0'.format(history_json["WalletCode"],history_json['StartDate'],history_json['EndDate'])
    header = {'InstallationID':InstallationID, "Authorization":AUTH, "DeviceId":device_id, "AppId":APP_ID, "Content-Type": 'application/json', 'Accept': 'application/json'}
    response = requests.get(url, headers=header).json()
    return response['ListOfObjects']








