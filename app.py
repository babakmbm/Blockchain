from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()


@app.route('/mine_Block', methods=['GET'])
def mine_block():
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


@app.route('/get_full_chain', methods=['GET'])
def get_full_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)
                }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
