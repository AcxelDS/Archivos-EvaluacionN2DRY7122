import requests
import json

api_key = "EA3tzSdjOV8AyAyJO286vNBt4Dz1b6j6"

while True:
    origin = input("Ingrese el lugar de partida (o 'q' para salir): ")
    if origin.lower() == "q":
        break
    destination = input("Ingrese el lugar de destino: ")

    url = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={origin}&to={destination}&unit=k"

    response = requests.get(url)

    data = json.loads(response.text)
    route = data["route"]
    legs = route["legs"]
    distance = legs[0]["distance"]
    duration = legs[0]["formattedTime"]

    fuel = distance / 10

    language = "es"
    url_instructions = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={origin}&to={destination}&unit=k&locale={language}"
    response_instructions = requests.get(url_instructions)
    data_instructions = json.loads(response_instructions.text)
    maneuvers_instructions = data_instructions["route"]["legs"][0]["maneuvers"]

    print(f"Distancia total: {distance:.2f} kilómetros")
    print(f"Duración estimada del viaje: {duration}")
    print(f"Combustible requerido: {fuel:.2f} litros")

    print("Narrativa del viaje:")
    for maneuver in maneuvers_instructions:
        print(maneuver["narrative"])

print("¡Gracias por usar el programa!")
