import requests
from config.constants import API_URL
import click
import json

def health_check():
    try:
        response = requests.get(f"{API_URL}/health")
        if response.status_code == 200:
            data = response.json()
            
            if 'message' in data:
                return data['message']
            else:
                print("Error: 'message' key not found in the response JSON.")
                return None
    except requests.exceptions.Timeout:
        click.echo(f"Error: Request to {API_URL}/health timed out.", err=True)
        return None
    except requests.exceptions.RequestException as e:
        click.echo(f"Error connecting to API at {API_URL}/health: {e}", err=True)
        return None
    except json.JSONDecodeError:
        click.echo(f"Error: Failed to decode JSON response from {API_URL}/health.", err=True)

        return None
    except Exception as e:
        click.echo(f"An unexpected error occurred during health check: {e}", err=True)
        return None