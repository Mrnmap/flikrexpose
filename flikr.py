import requests
import json

def format_json(response_text):
    # Format JSON response for better readability
    try:
        json_data = json.loads(response_text)
        formatted_json = json.dumps(json_data, indent=2)
        return formatted_json
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {e}"

def highlight_sensitive_info(response_text, sensitive_info):
    # Highlight sensitive information in the response text
    return response_text.replace(sensitive_info, f"\033[1;31;47m{sensitive_info}\033[m")

def get_recent_photos(api_key):
    # Flickr API endpoint URLs
    url1 = f"https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key={api_key}&page=1&format=json&nojsoncallback=1&extras=url_w"
    url2 = f"https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key={api_key}&format=json&nojsoncallback=1"

    try:
        # Make requests to Flickr API
        response1 = requests.get(url1)
        response2 = requests.get(url2)

        # Format and display results with highlighted sensitive information
        print("\033[1;33;40mFlickr API Key Exposure by VKS\033[m")
        print("\nResponse from URL 1:")
        formatted_response1 = format_json(response1.text)
        print(highlight_sensitive_info(formatted_response1, api_key))

        print("\nResponse from URL 2:")
        formatted_response2 = format_json(response2.text)
        print(highlight_sensitive_info(formatted_response2, api_key))

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("\033[1;31;40mFlickr API Key Exposure Tool (mrnmap)\033[m")
    # Get Flickr API key from user input
    flickr_api_key = input("Enter your Flickr API key: ")

    # Call the function with the user-provided API key
    get_recent_photos(flickr_api_key)
