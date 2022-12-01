import requests 

api_url = "http://127.0.0.1:5000/predict"




def test100Times(jsonInput):
    totalTime = 0
    for x in range(100):
        response = requests.post(api_url, json=jsonInput)
        
        totalTime += response.elapsed.total_seconds()
        
    average = totalTime / 100
    
    print(average)
        
    
    


jsonInput = {"text": "Emperor of Mars has declared war on Earth"}
test100Times(jsonInput)


jsonInput = {"text": "Rainey Fu received 10/10 on lab 7"}
test100Times(jsonInput)




jsonInput = {"text": "The Earth is still round"}
test100Times(jsonInput)



jsonInput = {"text": "Queen Elizabeth II has died"}
test100Times(jsonInput)



jsonInput = {"text": "Fifty year old man finishes a marathon!"}
test100Times(jsonInput)


jsonInput = {"text": "Canada becomes USA's 51st state!"};
test100Times(jsonInput)