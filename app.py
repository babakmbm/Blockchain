from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()


@app.route('/Mine_A_Block', methods=['GET'])
def mine_a_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    block = blockchain.createBlock(proof=proof, previous_hash=blockchain.hash(previous_block))

    response = {'message': 'A block was mined!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']
                }

    return jsonify(response), 200
