from django.shortcuts import render
from openai import OpenAI
import os

api_path = './api_key.txt'
def read_api_key(file_path=api_path):
    try:
        with open(file_path, 'r') as file:
            api_key = file.read().strip()
        return api_key
    except FileNotFoundError:
        print(f"파일 '{file_path}'을 찾을 수 없습니다.")
        return None
txt_api_key = read_api_key()

client = OpenAI(api_key=txt_api_key)
<<<<<<< HEAD
# Create your views here.


=======
>>>>>>> 47016c2a73fd56619cc84c35848e3b97fbc7e15a


#chatGPT에게 채팅 요청 API
def chatGPT(prompt):
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])
    print(completion)
    result = completion.choices[0].message.content
    return result

#chatGPT에게 그림 요청 API
def imageGPT(prompt):
    response = client.images.generate(prompt=prompt,
    n=1,
    size="256x256")
    result =response['data'][0]['url']
    return result

def index(request):
    return render(request, 'gpt/index.html')

def chat(request):
    #post로 받은 question
    prompt = request.POST.get('question')


    #type가 text면 chatGPT에게 채팅 요청 , type가 image면 imageGPT에게 채팅 요청
    result = chatGPT(prompt)

    context = {
        'question': prompt,
        'result': result
    }

    return render(request, 'gpt/result.html', context) 

def result_test(request):
   
    context = {
        'question': 'hello',
        'result': 'answer test'
    }
   
    return render(request, 'gpt/result.html', context)