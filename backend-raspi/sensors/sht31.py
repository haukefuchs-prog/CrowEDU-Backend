from smbus2 import SMBus
import time

SHT31_ADDR = 0x44

def read_sensor():
    with SMBus(1) as bus:
        bus.write_i2c_block_data(SHT31_ADDR, 0x24, [0x00])
        time.sleep(0.02)

        data = bus.read_i2c_block_data(SHT31_ADDR, 0x00, 6)

        temp_raw = (data[0] << 8) | data[1]
        hum_raw = (data[3] << 8) | data[4]

        temperature = -45 + (175 * temp_raw / 65535.0)
        humidity = 100 * hum_raw / 65535.0

        return temperature, humidity