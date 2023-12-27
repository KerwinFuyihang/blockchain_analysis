# Blockchain Analysis Project

## Overview
This project aims to provide a comprehensive analysis of blockchain technologies, focusing on their efficiency, security, and decentralization aspects. It includes comparative studies of systems like Algorand and Beaconchain, offering insights into the blockchain trilemma.

## Features
- Comparative analysis of blockchain systems
- Quantitative measurements of decentralization, efficiency, and security
- Data-driven insights into blockchain technologies

## Data
### Data preparation
Acquire Algorand data from [Bitquery](https://bitquery.io/), and acquire Beacon data from [Beacon Explorer](https://beaconcha.in/) by using SIPDER framework. 

The data was stored in the [Algorand_data](https://github.com/chengnanyimeng/blockchain_analysis/tree/main/Algorand_data) and [Beacon_chain_data](https://github.com/chengnanyimeng/blockchain_analysis/tree/main/Beacon_chain_data) 
### Data dictionary
We evaluate the decentralization in two layers, the consensus layer and the transaction layer.

For the consensus layer, we use proposer/validator data to represent the staking or voting process.
#### Proposer data (Algorand)
| Column Name      | Discription                                                                                               |
|------------------|----------------------------------------------------------------------------------------------------------------|
| `date`           | The specific date for which the data is recorded, formatted as "YYYY-MM-DD".                                   |
| `proposer_count` | The number of proposers that participated in the block proposal process on the given date.        |
| `reward`         | The reward given to the proposers or validators on that date, possibly denoted in the native cryptocurrency.   |

#### Validator data (Beacon)
Placeholder here.

For the transaction layer, we use the number of daily transaction data to quantify the decentralization.
#### Beacon transaction data
| Column Name | Discription                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------|
| `Timestamp` | The timestamp when the transactions were recorded             |
| `Value`     | The total number of transactions processed on the Algorand for the corresponding timestamp.    |

#### Algorand transaction data
placehoder here.





## Methodologies to quantify on-chain decentralization
### Shannon Entropy

### Gini Coefficient

### Nakaoto Coefficient

### Herfindahl Hirschman Index

## Usage
Guidelines on how to use the project, including any necessary commands or scripts.

## Contributing
Information on how others can contribute to the project.

## License
Details about the project's licensing.

## Contact
Information for contacting the project maintainers for further queries or collaborations.

