import csv

# Read cvs file
with open('al_block_data_proposercount_reward.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  
    column_index = 1  

    # read column data
    column_data = [row[column_index] for row in csv_reader]

    # comma seperated
    csv_string = ','.join(column_data)

    # output
    with open('output_proposer.txt', 'w') as output_file:
        output_file.write(csv_string)
