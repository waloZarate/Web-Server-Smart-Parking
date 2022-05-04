import os

import paho.mqtt.client as mqtt
from flask import Flask, render_template, request, redirect, make_response
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS
import eventlet
import datetime             #Show date
import csv                  #for storing data
import time

import socketio                 

eventlet.monkey_patch()
app = Flask(__name__)
app.config['SECRET_KEY'] = ''
socketio = SocketIO(app, ping_interval=5, ping_timeout=10)
CORS(app)

#The callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    
    # Subscribing in on_connect()means that if we lose the conection
    # and reconnect then subscrioptions will be renewed.
    
    client.subscribe("nodo1/espacio1/dist1")
    client.subscribe("nodo1/espacio1/ocu1")
    client.subscribe("nodo1/espacio1/dispo1")
    client.subscribe("nodo1/espacio1/reservado1")
    
    client.subscribe("nodo1/espacio2/dist2")
    client.subscribe("nodo1/espacio2/ocu2")
    client.subscribe("nodo1/espacio2/dispo2")
    client.subscribe("nodo1/espacio2/reservado2")
    
    client.subscribe("nodo1/espacio3/dist3")
    client.subscribe("nodo1/espacio3/ocu3")
    client.subscribe("nodo1/espacio3/dispo3")
    client.subscribe("nodo1/espacio3/reservado3")
    
    client.subscribe("nodo1/espacio4/dist4")
    client.subscribe("nodo1/espacio4/ocu4")
    client.subscribe("nodo1/espacio4/dispo4")
    client.subscribe("nodo1/espacio4/reservado4")
    
    #The callback for when a PUBLISH mesage is received from the ESP
    
def on_message(client, userdata, message):
    socketio.emit("my variable")
    print("Received message '" + str(message.payload) + "' on topic '" 
            + message.topic + "' with QoS " + str(message.qos))
    
     # ESPACIO 1
     
    if message.topic == "nodo1/espacio1/dist1":
        global distancia1
        distancia1 = str(message.payload.decode('utf-8'))
        print("Distancia update " + distancia1)
        socketio.emit('hc-sr04_distancia', {'data': message.payload})
        
    if message.topic == "nodo1/espacio1/ocu1":
        global ocupado1
        ocupado1 = str(message.payload.decode('utf-8'))
        print("Ocupado update " + ocupado1)
        socketio.emit('ledRojo_1', {'data': message.payload})
        
    if message.topic == "nodo1/espacio1/dispo1":
        global disponible1
        disponible1 = str(message.payload.decode('utf-8'))
        print("Disponible update " + disponible1)
        socketio.emit('ledVerde_1', {'data': message.payload})
        
    if message.topic == "nodo1/espacio1/reservado1":
        global reserva1
        reserva1 = str(message.payload.decode('utf-8'))
        print("Reserva update " + reserva1)
        socketio.emit('ledAzul_1', {'data': message.payload})
        
     # ESPACIO 2
        
    if message.topic == "nodo1/espacio2/dist2":
        global distancia2
        distancia2 = str(message.payload.decode('utf-8'))
        print("Distancia update " + distancia2)
        socketio.emit('hc-sr04_distancia2', {'data': message.payload})
        
    if message.topic == "nodo1/espacio2/ocu2":
        global ocupado2
        ocupado2 = str(message.payload.decode('utf-8'))
        print("Ocupado update " + ocupado2)
        socketio.emit('ledRojo_2', {'data': message.payload})
        
    if message.topic == "nodo1/espacio2/dispo2":
        global disponible2
        disponible2 = str(message.payload.decode('utf-8'))
        print("Disponible update " + disponible2)
        socketio.emit('ledVerde_2', {'data': message.payload})
        
    if message.topic == "nodo1/espacio2/reservado2":
        global reserva2
        reserva2 = str(message.payload.decode('utf-8'))
        print("Reserva update " + reserva2)
        socketio.emit('ledAzul_2', {'data': message.payload})
   
      # ESPACIO 3
      
    if message.topic == "nodo1/espacio3/dist3":
        global distancia3
        distancia3 = str(message.payload.decode('utf-8'))
        print("Distancia update " + distancia3)
        socketio.emit('hc-sr04_distancia3', {'data': message.payload})
        
    if message.topic == "nodo1/espacio3/ocu3":
        global ocupado3
        ocupado3 = str(message.payload.decode('utf-8'))
        print("Ocupado update " + ocupado3)
        socketio.emit('ledRojo_3', {'data': message.payload})
        
    if message.topic == "nodo1/espacio3/dispo3":
        global disponible3
        disponible3 = str(message.payload.decode('utf-8'))
        print("Disponible update " + disponible3)
        socketio.emit('ledVerde_3', {'data': message.payload})
        
    if message.topic == "nodo1/espacio3/reservado3":
        global reserva3
        reserva3 = str(message.payload.decode('utf-8'))
        print("Reserva update " + reserva3)
        socketio.emit('ledAzul_3', {'data': message.payload})
        
      # ESPACIO 4
   
    if message.topic == "nodo1/espacio4/dist4":
        global distancia4
        distancia4 = str(message.payload.decode('utf-8'))
        print("Distancia update " + distancia4)
        socketio.emit('hc-sr04_distancia4', {'data': message.payload})
        
    if message.topic == "nodo1/espacio4/ocu4":
        global ocupado4
        ocupado4 = str(message.payload.decode('utf-8'))
        print("Ocupado update " + ocupado4)
        socketio.emit('ledRojo_4', {'data': message.payload})
        
    if message.topic == "nodo1/espacio4/dispo4":
        global disponible4
        disponible4 = str(message.payload.decode('utf-8'))
        print("Disponible update " + disponible4)
        socketio.emit('ledVerde_4', {'data': message.payload})
        
    if message.topic == "nodo1/espacio4/reservado4":
        global reserva4
        reserva4 = str(message.payload.decode('utf-8'))
        print("Reserva update " + reserva4)
        socketio.emit('ledAzul_4', {'data': message.payload})
            
            
# Initialize MQTT Broker

mqttc = mqtt.Client(client_id="capstone")
broker = '192.168.1.211'
port = 1883

print("connecting to broker ", broker)
# Launch MQTT
#mqttc.username_pw_set(username, password) #set user pass
#mqttc=mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv31)   

mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect(broker, port)
mqttc.loop_start()
time.sleep(1)


#Create a dictionary called "pins" to store the pin number, name, and pin state:

pins = {
   4 : {'name' : 'GPIO 4', 'board' : 'esp8266', 'topic' : 'esp8266/4', 'state' : 'False'},
   5 : {'name' : 'GPIO 5', 'board' : 'esp8266', 'topic' : 'esp8266/5', 'state' : 'False'}
   }

# Put the pin dictionary into the template data dictionary:
templateData = {
   'pins' : pins
   }

@app.route("/")
def main():
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', async_mode=socketio.async_mode, **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<board>/<changePin>/<action>")
def action(board, changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   devicePin = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "1" and board == 'esp8266':
      mqttc.publish(pins[changePin]["topic"],"1")
      pins[changePin]['state'] = 'True'

   if action == "0" and board == 'esp8266':
      mqttc.publish(pins[changePin]["topic"],"0")
      pins[changePin]['state'] = 'False'

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

@socketio.on('my event')
def handle_my_custom_event(json):
   print('received json data here: ' + str(json))

@socketio.on('my event1')
def handle_my_temperature(json):
   print('received json temperature here: ' + str(json))

@socketio.on('my event2')
def handle_my_humidity(json):
   print('received json humidity here: ' + str(json))

@socketio.on('my event3')
def handle_my_kwh(json):
   print('received json humidity here: ' + str(json))

if __name__ == "__main__":
       
   # opens and writes csv file
   with open('sensor.csv', mode='a+') as file:
      reader = csv.reader(file, delimiter=',')
      writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      line_count = 0
      time = datetime.datetime.now()
      #way to write to csv file
      for row in reader:
         if line_count == 0:
            writer.writerow(['date','time','temperature','humidity','energy'])
         else:
            writer.writerow([time.strftime("%x"),time.strftime("%X"),distancia1,ocupado1,disponible1,reserva1])

   socketio.run(app, host='0.0.0.0', port=8080, debug=True)
