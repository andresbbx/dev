from paho.mqtt import client as mqtt

# Crear un cliente MQTT
client = mqtt.Client()

# Establecer la conexión con el broker MQTT
client.connect("broker.emqx.io", 1883, 60)

# Publicar el mensaje
client.publish("artux/test", "Hola, mundo!")

# Desconectar el cliente
client.disconnect()
