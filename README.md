# DialogFlow
DialogFlow y Analisis de Sentimeintos

En este script hace uso de un proyecto en DialogFlow.
Para hacer uso de este es necesario tener un proyecto en DialogFlow a convenencia y colocarlo en la siguiente parte:
  El primer datos es el id de nuestro proyecto en dialog FLow.
  En segundo en un id generado por uds para hacer seguimiento de este script y dialog flow sepa de su continuacion y separar consultas.
  El tercer dato es el mensaje a mandar, queda a sujecion del proyecto a ver opciones a mandar.
  Por ultimo, en cuarto lugar, mandamos el lenguaje en que esta el mensaje mandado.
  
    detect_intent_with_sentiment_analysis("aqui escribes tu id del proyecto en dialogflow" ,"123456789", ["I am so happy and joyful."] ,"es")
    
 Nota: Para hacer uso de este script es necesario tener una facturacion en google cloud platform. mas informacion en https://cloud.google.com/
