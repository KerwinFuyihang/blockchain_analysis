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
| `reward`         | The Reward for block proposal per day.   |


#### Validator data (Beacon)
| Column Name      | Discription                                                                                               |
|------------------|----------------------------------------------------------------------------------------------------------------|
| `date`           | The specific date for which the data is recorded, formatted as "YYYY-MM-DD".                                   |
| `Value` | Average account balance of validators per day.      |

For the transaction layer, we use the number of daily transaction data to quantify the decentralization.
#### Beacon transaction data
| Column Name | Discription                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------|
| `Timestamp` | The timestamp when the transactions were recorded             |
| `daily_transaction`     | The daily transaction on Beacon (USD).    |

#### Algorand transaction data
| Column Name | Discription                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------|
| `time` | The timestamp when the transactions were recorded             |
| `count`     | Transaction count per day.    |
| `fees`     | Tokens used for transaction.    |

## Methodologies to quantify on-chain decentralization
### Shannon Entropy
A higher value indicates more chaos in authority distribution while a lower value refers to a more centralized system. We define the indice $H(v)$ as:
$$H(v) = \prod \limits_{i=1}^N P(v_i)^{-P(v_i)}$$
where the $v_i$ refers to the unit data for each layer and the $P(v_i)$ refers to the weight of the unit data in respect to the overall dataset:
$$P(v_i) = \frac{v_i}{\sum_{i=1}^N v_i}$$

### Gini Coefficient
$$G = 1 - \sum_{i=1}^N P_i^2$$
### Nakaoto Coefficient
$$ N = min\{k \in [1,...,K] : \sum_{i=1}^K P_i > 0.51\}$$
### Herfindahl Hirschman Index
$$HHI = \sum_{i=1}^N P_i^2$$
## Usage
To execute the Jupyter Notebook and perform the analysis:
1. Navigate to the directory where you cloned the repository.
2. Start the Jupyter Notebook server by running `jupyter notebook` in your command line.
3. Open the `experiment.ipynb` file from the Jupyter Notebook interface in your browser.
4. Execute the notebook cells in sequence to conduct the analysis.

## Contributing
We welcome contributions from the community. If you wish to contribute to the project, please follow these guidelines:
- Fork the repository and create a feature branch.
- Make your changes and ensure that your code adheres to the existing style.
- Submit a pull request with a clear description of your improvements or bug fixes.

## License
This project is licensed under [MIT License]. For more details, see the LICENSE file in the repository.

## Contact
For any inquiries or potential collaborations, please reach out to the project maintainers at [lz183@duke.edu]. We are open to feedback and interested in hearing about how you may want to use or improve the project.
