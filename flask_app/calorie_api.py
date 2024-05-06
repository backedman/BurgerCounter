import requests

class NutritionNinjaAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.api-ninjas.com/v1/nutrition'

    def __call__(self, query):
        api_url = f"{self.base_url}?query={query}"
        headers = {'X-Api-Key': self.api_key}
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()[0]['calories']
        except requests.exceptions.RequestException as e:
            print("Error occurred during API request:", e)
            return None

if __name__ == '__main__':
    # Example usage:
    api_key = 'Uv9UoG21C7OMpfjhmJTSeA==U77gFRDxSkovYvgz'
    query = '1lb brisket and fries'
    nutrition_api = NutritionNinjaAPI(api_key)
    response_data = nutrition_api(query)
    if response_data:
        print(response_data)
    else:
        print("Error occurred while fetching nutritional information.")
