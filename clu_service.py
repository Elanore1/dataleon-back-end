from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

class CluService:
    ''' 
    Class that retrieves the intent from CLU engine

    Arguments:
        - prediction_key : Our CLU prediction key
        - endpoint : endpoint url of the api CLU engine
    ''' 
    def __init__(self, endpoint, subscription_key):
        self.endpoint = endpoint
        self.credential = AzureKeyCredential(subscription_key)
        self.client = ConversationAnalysisClient(self.endpoint, self.credential)
    ''' 
    Method that return the intent of the CLU engine

    Arguments:
        - utterance : The utterance to analyse
    ''' 
    def get_intent(self,utterance):
        with self.client :
            result = self.client.analyze_conversation(
                task = {
                    "kind": "Conversation",
                    "analysisInput": {
                        "conversationItem": {
                            "participantId": "1",
                            "id": "1",
                            "modality": "text",
                            "language": "en",
                            "text": utterance
                        },
                        "isLoggingEnabled": False
                    },
                    "parameters": {
                        "projectName": "dataleon-CLU-engine", #CLU project name
                        "deploymentName": "deployement1", #CLU deployement name
                        "verbose": True
                    }
                }
            )
            print(result)
        return result