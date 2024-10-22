# Fungsi untuk mengkonversi suhu antara Celsius dan Fahrenheit
def konversisuhu(temperature, value) :
    # Jika value = 'C', konversi dari Fahrenheit ke Celsius
    if value == 'C' :
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'
    # Jika tidak, konversi dari Celsius ke Fahrenheit
    else : 
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'F'

# Contoh konversi dari Celsius ke Fahrenheit
celsius_temperature = 30 # Suhu awal dalam Celsius
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')
# Menampilkan hasil konversi Celsius ke Fahrenheit
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")
# Contoh konversi dari Fahrenheit ke Celsius
fahrenheit_temperature = 86  # Suhu awal dalam Fahrenheit
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
# Menampilkan hasil konversi Fahrenheit ke Celsius
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")