import pytest # importing pytest library
from clu_service import CluService # importing our CluService class

## Create a new Language service ressource on Azure AI services
## Replace this value with your actual endpoint and API key
endpoint = 'https://en-language-ressource.cognitiveservices.azure.com/'
subscription_key = 'ec402379800449999dd695862b146b7a'

@pytest.fixture # test fixture decorator
def clu_service():
    return CluService(endpoint, subscription_key) # creating an instance of our clu service
 
# creating parametrize tests decorator 
@pytest.mark.parametrize("utterance", [ ('How to make an Hamburger?'), ('Best Indian Samosa recipe'), ('What is the best peach cake?'), ('How many liter of milk in pancake')])

# test for testing that the TopIntent is from recipe cooking 
def test_get_intent(clu_service, utterance):
    try : 
        response = clu_service.get_intent(utterance)
        # Check for topIntent = Recipe
        assert 'Recipe' in response["result"]["prediction"]["topIntent"]
    except Exception as e :
        print(f"Error during test: {e}")
        assert False # If error test return false
 
@pytest.mark.parametrize("utterance1", [('Best Indian Samosa recipe')])
# test for testing the entity CuisineType in the utterance        
def test_cuisineType_entity(clu_service, utterance1):
    try : 
        response = clu_service.get_intent(utterance1)
        print(response)
        # Check for CuisineType entity
        entities = response.get("result", {}).get("prediction", {}).get("entities", [])
        assert 'CuisineType' in [entity.get("category", "") for entity in entities]
    except Exception as e :
        print(f"Error during test: {e}")
        assert False
  
@pytest.mark.parametrize("utterance2", [('How to make a pizza for 4 peoples')])
# test for testing the entity Quantity in the utterance        
def test_quantity_entity(clu_service, utterance2):
    try : 
        response = clu_service.get_intent(utterance2)
        print(response)
        # Check for Quantity entity
        entities = response.get("result", {}).get("prediction", {}).get("entities", [])
        assert 'Quantity' in [entity.get("category", "") for entity in entities]
    except Exception as e :
        print(f"Error during test: {e}")
        assert False

@pytest.mark.parametrize("utterance3", [('Best peach cake recipe')])
# test for testing the entity Ingredients in the utterance        
def test_ingredients_entity(clu_service, utterance3):
    try : 
        response = clu_service.get_intent(utterance3)
        print(response)
        # Check for Ingredients entity
        entities = response.get("result", {}).get("prediction", {}).get("entities", [])
        assert 'Ingredients' in [entity.get("category", "") for entity in entities]
    except Exception as e :
        print(f"Error during test: {e}")
        assert False
        
@pytest.mark.parametrize("utterance4", [('Pizza marguerita')])
# test for testing the entity Dishname in the utterance        
def test_dishName_entity(clu_service, utterance4):
    try : 
        response = clu_service.get_intent(utterance4)
        print(response)
        # Check for Dishname entity
        entities = response.get("result", {}).get("prediction", {}).get("entities", [])
        assert 'DishName' in [entity.get("category", "") for entity in entities]
    except Exception as e :
        print(f"Error during test: {e}")
        assert False