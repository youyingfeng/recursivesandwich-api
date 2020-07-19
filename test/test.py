import requests

# req = requests.get('http://localhost:3000/highscores')
# print(req.text)

post = requests.post('http://localhost:3000/highscores',
                      data = {'user': 'lmao', 'time': 95})
print(post.text)
print('Complete!')