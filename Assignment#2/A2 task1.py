import requests
with open("api.txt",'r') as file:
    apiUrl=file.read()
    try:
        response=requests.get(apiUrl)
        if response.status_code==200:
            data=response.json()
            if data.get("status")=="success" and "data" in data and data["data"]:
                matchlist=data['data']
                print("API Status:")
                print(data['info'])
                for match in matchlist:
                    print("---------------------")
                    print(f'Match Name: {match['name']}')
                    print(f'Match Status: {match['status']}')
                    print(f'venue: {match['venue']}')
                    print(f'Date: {match['date']}')
                    if 'score' in match:
                        for score in match['score']:
                            print()
                            print(f'Inning: {score['inning']}')
                            print(f'Runs: {score['r']}')
                            print(f'Wickets: {score['w']}')
                            print(f'Overs: {score['o']}')
            else:
                errorMessage=data.get("reason","No live matches found or an unknown error occurred.")
                print(f"Could not retrieve matches:{errorMessage}")

        else:
            print(f"Error: Failed to fetch data. Status Code:{response.status_code}")
            print("Response:",response.text)
    except requests.exceptions.RequestException as e:
        print(f"A network error occured:{e}")
