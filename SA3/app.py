from flask import Flask, render_template, request
import os
from time import time
from blockchain import BlockChain, Block
STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

chain = BlockChain()
# SA3: Set currentBlock to none to show no block has been created yet.
currentBlock = None

@app.route("/", methods= ["GET", "POST"])
def home():
    # SA3: Access currentBlock as global
    global blockData, currentBlock, chain
    
    if request.method == "GET":
        return render_template('index.html')
    else:
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        artId = request.form.get("artId")
        amount = request.form.get("price")
        
        transaction = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount,
                "artId": artId
            }  

        index = chain.length()
        if index==0:
            index = 1
        
        # SA3: Remove transaction key from blockData. 
        blockData = {
                'index': index,
                'timestamp': time(),
                'previousHash': "No Previous Hash.",
        }   
        
        # SA3: If no block exists then create new block
        if currentBlock == None:
            # SA3: Remove passing transaction to Block() constructor and move it inside the if condition
            currentBlock = Block(
                            blockData["index"], 
                            blockData["timestamp"], 
                            blockData["previousHash"])
        
        # SA3: Receive status of the currentBlock
        status = currentBlock.addTransaction(transaction)
        
        # SA3: Check block status after adding transaction, if block is ready then add the block to the blockchain
        # and make currentBlock variable None 
        if status == "Ready":
            chain.addBlock(currentBlock)   
            isValid = chain.validateBlock(currentBlock)
            currentBlock.isValid = isValid
            
            # SA3: Set currentBlock to none
            currentBlock = None
        
        chain.printChain()

        
    return render_template('index.html', blockChain = chain)


@app.route("/blockchain", methods= ["GET", "POST"])
def show():
    global chain, currentBlock

    currentBlockLength  = 0
    if currentBlock:
        currentBlockLength = len(currentBlock.transactions)
    
    return render_template('blockchain.html', blockChain = chain.chain, currentBlockLength = currentBlockLength)
    
if __name__ == '__main__':
    app.run(debug = True, port=4001)