import csv

# 读取CSV文件
with open('al_block_data_proposercount_reward.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # 跳过标题行
    column_index = 1  # 假设要导出第三列数据，索引从0开始

    # 提取指定列数据
    column_data = [row[column_index] for row in csv_reader]

    # 转换为逗号分隔的字符串
    csv_string = ','.join(column_data)

    # 导出数据
    with open('output_proposer.txt', 'w') as output_file:
        output_file.write(csv_string)
