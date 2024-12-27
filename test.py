import subprocess
import re

def extract_numbers(input_string):
    # 使用正则表达式查找所有数字
    numbers = re.findall(r'\d+', input_string)
    # 将字符串转换为整数
    return [int(num) for num in numbers]

# 获取显卡的显存
def get_integrated_memory():
    total_memory = 0
    # 通过wmic获取集成显卡信息
    result = subprocess.check_output('wmic path win32_videocontroller get adapterram', shell=True)
    # 解码字节串为字符串
    result_str = result.decode('utf-8')
    tempmem = extract_numbers(result_str)
    for m in tempmem:
        total_memory += m
    
    return total_memory / (1024 ** 2)

total_memory = get_integrated_memory()
print(f"总显存: {total_memory:.2f} MB")
