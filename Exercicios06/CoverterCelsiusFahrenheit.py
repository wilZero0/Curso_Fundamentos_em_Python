
def converter_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_fahrenheit = converter_para_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C equivalem a {temp_fahrenheit:.1f}°F.")
