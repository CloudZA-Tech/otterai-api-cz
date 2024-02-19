from otterai import OtterAI, OtterAIException
from django.http import JsonResponse


# Create your views here.
otter = OtterAI()
def login(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        otter.login(email, password)
        return JsonResponse({'status': 'success', 'message': 'Login successful'})
    except OtterAIException as e:
        return JsonResponse({'status': 'error', 'message': e})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': e})
    
    
def all_speeches(request):
    try:
        # found this to work to get the transcript alone from the data output when you use 'speech = otter.get_speech'
        speech = otter.get_speeches()
        speech_data = speech['data']
        return JsonResponse(speech_data)
    except OtterAIException as e:
        return JsonResponse({"OtterAI Exception occurred:", e})
    except Exception as e:
        return JsonResponse({"An unexpected error occurred:", e})
    

def speech_by_id(request):
    try:
        speech_index = request.GET.get('speech_id')
        speech = otter.get_speech(speech_index)
        speech_text = speech['data']
        speech_id = speech_text['speech']['speech_id']
        speech_title = speech_text['speech']['title']
        transcript_data = speech_text['speech']['transcripts'][0]['transcript']
        
        data = {
            "speech_id": speech_id,
            "speech_title": speech_title,
            "transcript": transcript_data
        }
        return JsonResponse(data)
    except OtterAIException as e:
        return JsonResponse({"OtterAI Exception occurred:", e})
    except Exception as e:
        return JsonResponse({"An unexpected error occurred:", e})