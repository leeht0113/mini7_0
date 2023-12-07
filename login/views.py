from django.shortcuts import render
from openai import OpenAI

client = OpenAI(api_key="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")
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, UserProfileForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')  # 회원가입 후 리다이렉트할 페이지 이름을 설정하세요.
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()
    return render(request, 'signup.html', {'form': form, 'profile_form': profile_form})

def home(request):
    return render(request, 'home.html')  # 홈 페이지 템플릿을 작성하여 리다이렉트할 페이지로 사용하세요.



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
    return render(request, 'login/index.html')

def chat(request):
    #post로 받은 question
    prompt = request.POST.get('question')


    #type가 text면 chatGPT에게 채팅 요청 , type가 image면 imageGPT에게 채팅 요청
    result = chatGPT(prompt)

    context = {
        'question': prompt,
        'result': result
    }

    return render(request, 'login/result.html', context) 