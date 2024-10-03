import requests
from concurrent.futures import ThreadPoolExecutor
import time

# Define the target URL
url = input("Enter the target URL (e.g., http://example.com): ")

# Number of requests
total_requests = 10000

# Function to send a single HTTP request
def send_request(session, url):
    try:
        response = session.get(url)
        print(f"Request completed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

# Start timing
start_time = time.time()

# Use a session to make the requests more efficient
with requests.Session() as session:
    # Use ThreadPoolExecutor to run multiple requests in parallel
    with ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(send_request, session, url) for _ in range(total_requests)]

# Print the time taken to send all requests
end_time = time.time()
print(f"Completed {total_requests} requests in {end_time - start_time:.2f} seconds")
