"""Returns the result of detect intent with texts as inputs and analyzes the
sentiment of the query text.

Using the same `session_id` between requests allows continuation
of the conversation."""
import json
from google.cloud import dialogflow

def detect_intent_with_sentiment_analysis(project_id, session_id, texts, language_code):
    
    session_client = dialogflow.SessionsClient()

    session_path = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session_path))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        # Enable sentiment analysis
        sentiment_config = dialogflow.SentimentAnalysisRequestConfig(
            analyze_query_text_sentiment=True
        )

        # Set the query parameters with sentiment analysis
        query_params = dialogflow.QueryParameters(
            sentiment_analysis_request_config=sentiment_config
        )

        response = session_client.detect_intent(
            request={
                "session": session_path,
                "query_input": query_input,
                "query_params": query_params,
            }
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
        # Score between -1.0 (negative sentiment) and 1.0 (positive sentiment).
        print(
            "Query Text Sentiment Score: {}\n".format(
                response.query_result.sentiment_analysis_result.query_text_sentiment.score
            )
        )
        print(
            "Query Text Sentiment Magnitude: {}\n".format(
                response.query_result.sentiment_analysis_result.query_text_sentiment.magnitude
            )
        )
        #imprime todo el contenido el request json con los datos
        print (response)

detect_intent_with_sentiment_analysis("aqui escribes tu id del proyecto en dialogflow"
                    ,"123456789"
                    ,["I am so happy and joyful."]
                    ,"es")
