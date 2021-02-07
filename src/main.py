"""
Main file of package
"""

from src.three_tabke_join import three_table_result
from src.two_table_join import two_table_result

result = {}
two_table_joint_output = two_table_result()
three_table_joint_output = three_table_result()

print("Join table which has 1k data each")
result["1000_two"] = two_table_joint_output(1000)
result["1000_three"] = three_table_joint_output(1000)

print("Join table which has 10k data each")
result["10000_two"] = two_table_joint_output(10000)
result["10000_three"] = three_table_joint_output(10000)

print("Join table which has 100k data each")
result["100000_two"] = two_table_joint_output(100000)
result["100000_three"] = three_table_joint_output(100000)

print("Join table which has 1M data each")
result["1000000_two"] = two_table_joint_output(1000000)
result["1000000_three"] = three_table_joint_output(1000000)

print("Query Time taken result")
print(result)
