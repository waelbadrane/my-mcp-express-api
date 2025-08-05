
import requests

def create_dfn():
    url = 'https://your-api-endpoint.com/CreateDfnAPI'  # Update with your actual endpoint
    payload = {
        # Add any required request body parameters here
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        test_id = data.get('testId')  # Adjust property name as per API response
        print('Test ID:', test_id)
        return test_id
    except requests.RequestException as e:
        print('Error creating DFN:', e)
        return None
