from machine import I2C, Pin
import ssd1306
import time
import imu

#grove port
i2c = I2C(scl = Pin(32), sda = Pin(26))
#uncomment for back pins
#i2c = I2C(scl = Pin(21), sda = Pin(25))

oled = ssd1306.SSD1306_I2C(128,32, i2c)
imu0 = imu.IMU()


while True:
    data = str(imu0.acceleration)
    oled.text(data,0,0,1)
    oled.show()
    time.sleep_ms(100)
    oled.fill(0)
    
