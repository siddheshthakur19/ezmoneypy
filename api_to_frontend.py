__author__ = 'surajman'

from flask import Flask, jsonify, request, abort, app
import api_to_backend as atb



@app.route('/ezmoney/api/v1.0/InDaCribMuthafuckaaaa', methods=['POST'])
def register_new_user():
    if not request.json or any("FirstName","Surname","DateOfBirth","Gender","DisplayName","Email", "PushID", "WalletType", "PhoneNumber", "DeviceID") not in request.json:
        abort(400)
    user_json = request.json
    install_id, status = atb.register_new_member(user_json) # 201 - all good, 001 - idk, 999 - error
    return jsonify({"InstallationID":install_id, "Status":status})


@app.route('/ezmoney/api/v1.0/Hustlin', methods=['POST'])
def create_new_wallet():
    if not request.json or any("InstallationID", "WalletName", "TopUpFrequency", "AccountNo", "DeviceID") not in request.json:
        abort(400)
    wallet_code, status = atb.create_wallet(request.json)
    return jsonify({"WalletCode":wallet_code, "Status":status})


@app.route('/ezmoney/api/v1.0/RollinInDatGreen', methods=['POST'])
def get_wallet_info():
    if not request.json or any("InstallationID","WalletCode", "DeviceID") not in request.json:
        abort(400)
    wallet_info, status = atb.get_wallet_info(request.json)
    return jsonify(**wallet_info)


@app.route('/ezmoney/api/v1.0/WhereMyGreenAt', methods=['POST'])
def get_wallet_list():
    if not request.json or any("InstallationID","DeviceID") not in request.json:
        abort(400)
    wallet_list, status = atb.get_wallet_list(request.json)
    return jsonify(**wallet_list)


@app.route('/ezmoney/api/v1.0/PayDayBitchez', methods=['POST'])
def do_topup():
    if not request.json or any("InstallationID","DeviceID","WalletCode","Date","Amount","Reason") not in request.json:
        abort(400)
    status = atb.top_up(request.json)
    return status


@app.route('/ezmoney/api/v1.0/PityDatFool', methods=['POST'])
def merch_init_pay():
    if not request.json or any("InstallationID","DeviceID","WalletCode","Amount","Description") not in request.json:
        abort(400)
    pay_token = atb.merch_req_pay(request.json)
    return pay_token


#Called when payment token is received and consumer clicks 'OK'
@app.route('/ezmoney/api/v1.0/YouTrippinFool', methods=['POST'])
def confirm_payment():
    if not request.json or any("InstallationID","DeviceID","PaymentToken","PIN") not in request.json:
        abort(400)
    status = atb.confirm_payment(request.json)
    return status


@app.route('/ezmoney/api/v1.0/NiggaFromAnothaMotha', methods=['POST'])
def pay_my_nigga():
    if not request.json or any("InstallationID","DeviceID","SrcWallet","DestWallet","Amount","Date","Reason") not in request.json:
        abort(400)
    status = atb.transfer_between_wallets(request.json)
    return status


@app.route('/ezmoney/api/v1.0/TransactionHistory', methods=['POST'])
def history():
    if not request.json or any("InstallationID","DeviceID","WalletCode","StartDate","EndDate") not in request.json:
        abort(400)
    transaction_list = atb.get_transaction_history(request.json)
    return jsonify(**transaction_list)













