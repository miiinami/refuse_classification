import pycuda.driver as cuda
import pycuda.autoinit

# 获取所有可用的设备
device_count = cuda.Device.count()
total_memory = 0

for i in range(device_count):
    device = cuda.Device(i)
    total_memory += device.total_memory() // (1024**2)  # 转换为MB

print(f"总显存大小: {total_memory} MB")
