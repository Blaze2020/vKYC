# To perform small middeleware options
import json

from blockchain.BlockChain import BlockChain

userData = []


def extractname(email):
    if '.' in email.split('@')[0]:
        return email.split('@')[0].replace('.', '')
    else:
        return email.split('@')[0]


def storeData(blockchain, data):
    print("***Mining about to start***")
    # print(blockchain.chain)

    last_block = blockchain.latest_block
    last_proof_no = last_block.proof_no
    proof_no = blockchain.proof_of_work(last_proof_no)

    blockchain.new_data(data)

    last_hash = last_block.calculate_hash
    block = blockchain.construct_block(proof_no, last_hash)

    print("***Mining has been successful***")
    # print(blockchain.chain)
    print_data(blockchain.chain)
    for block in blockchain.chain:
        userData.append(block.data)
    json_data = json.dumps(userData)

    with open('userData.json', 'a') as f:
        json.dump(json_data, f)

    # return blockchain.chain


def print_data(blockchain_data):
    for block in blockchain_data:
        print(block)
        print('----------------------------------------------------')


def proccessdata(blockchain, formdata):
    firstname = formdata.get('first_name').strip()
    lastname = formdata.get('last_name').strip()
    email = formdata.get('email').strip()
    phoneno = formdata.get('phone_no').strip()
    uid = formdata.get('uid').strip()  # UID,idcard,voterid,driving licence,NRI card
    pancard = str(formdata.get('pancard').upper().strip())
    address = formdata.get('address').strip()
    data = {'first_name': firstname,
            'last_name': lastname,
            'email': email,
            'phoneno ': phoneno,
            'pancard': pancard,
            'uid': uid,
            'address': address}
    print(data)

    storeData(blockchain, data)

    return True
