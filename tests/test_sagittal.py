import numpy as np
import os
from sagittal_brain.sagittal_brain import run_averages  # 假设你在 `sagittal_average` 包中定义了该函数

def test_something():
    # 创建测试输入数据
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1

    # 保存测试输入数据到文件
    input_file = "brain_sample.csv"
    output_file = "brain_average.csv"
    np.savetxt(input_file, data_input, fmt='%d', delimiter=',')

    # 定义期望的输出结果
    expected = np.zeros(20)
    expected[-1] = 1

    # 调用测试函数并生成输出文件
    run_averages(file_input=input_file, file_output=output_file)

    # 读取生成的结果
    result = np.loadtxt(output_file, delimiter=',')

    # 验证结果是否符合预期
    np.testing.assert_array_equal(result, expected)

    # 清理测试文件
    os.remove(input_file)
    os.remove(output_file)
