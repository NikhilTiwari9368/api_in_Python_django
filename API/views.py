from django.shortcuts import render
import requests


def fetch_posts(request):
    # Fetch data from the JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        posts = response.json()  # Parse the JSON response
    else:
        posts = []  # Fallback if the API call fails

    return render(request, 'posts.html', {'posts': posts}) 