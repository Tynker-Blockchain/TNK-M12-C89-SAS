from web3 import Web3

def getBlockData(blockNumber):
    # Start try block
    try:    
        # Set apiUrl to  'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
        apiUrl = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98' 
        # Create an instance of the HTTP provider
        web3 = Web3(Web3.HTTPProvider(apiUrl))
        # Fetching the block data from API
        apiBlockData = web3.eth.get_block(blockNumber)
    # Add except block    
    except:
            # set apiBlockData to "noBlock"
            apiBlockData ="noBlock"
            # return apiBlockData
            return apiBlockData
    # Create a dictionary named blockData
    blockData = {}
    # Storing basic details of block i.e difficulty, number, size, hash, parentHash 
    blockData['totalDifficulty'] = apiBlockData['difficulty']
    blockData['blockNumber'] = apiBlockData['number']
    blockData['size'] = apiBlockData['size']
    blockData['currentHash'] = apiBlockData['hash'].hex()
    blockData['previousHash'] = apiBlockData['parentHash'].hex()

    # Storing number of transaction details
    numberOfTransactions = len(apiBlockData['transactions'])
    blockData['numberOfTransactions'] = numberOfTransactions
  
    # Return the blockData
    return blockData

