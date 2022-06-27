import paho.mqtt.client
import time

def on_connect(client,userdata,flags,rc):
    print('connectado (%s)' % client._client_id)
    client.subscribe(topic="Temperatura",qos=1)

def on_message(client,userdata,message):
    print("-------------------------------")
    print('topico: %s'% message.topic)
    print('Menssagem: %s' % message.payload)


def publish(client):
        time.sleep(25)
        client.publish("Umidade"," Umidade: 94%",qos=1)

def main():
    client = paho.mqtt.client.Client(client_id="processo1",clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='127.0.0.1',port=1883)
    publish(client)
    client.loop_forever()

if __name__ == '__main__':
    main()