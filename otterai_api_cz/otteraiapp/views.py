from otterai import OtterAI, OtterAIException
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
otter = OtterAI()
@csrf_exempt
def login(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = otter.login(email, password)
        status = data['status']
        if status == 200:
            user = otter.get_user()
            username = user['data']['first_name'] + ' ' + user['data']['last_name']
            return JsonResponse({'logged in as': username, 'status': 'success', 'message': 'Login successful'})
        else:
            return JsonResponse({'status':data, 'message': 'Login failed'})
    except OtterAIException as e:
        return JsonResponse({'status': 'error', 'message': e}, safe=False)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': e},safe=False)
    
@csrf_exempt 
def all_speeches(request):
    try:
        # found this to work to get the transcript alone from the data output when you use 'speech = otter.get_speech'
        speech = otter.get_speeches()
        speech_data = speech['data']
        
        
        return JsonResponse(speech_data,safe=False)
    except OtterAIException as e:
        return JsonResponse({"OtterAI Exception occurred": e}, safe=False)
    except Exception as e:
        return JsonResponse({"An unexpected error occurred": e},safe=False)
    
@csrf_exempt
def speech_by_id(request):
    try:
        speech_index = request.POST.get('speech_id')
        speech = otter.get_speech(speech_index)
        if speech['status'] != 200:
            return JsonResponse({'status': speech['status'], 'message': 'Speech not found'})
        speech_text = speech['data']
        speech_id = speech_text['speech']['speech_id']
        speech_title = speech_text['speech']['title']
        transcript_data = speech_text['speech']['transcripts']
        speakers = speech_text['speech']['speakers']
        speech_outline = speech_text['speech']['speech_outline']
        
        speech_summary = []
        for item in speech_outline:
            if 'segments' in item:
                for segment in item['segments']:
                    speech_summary.append(segment['text'])  
            
        speakers_map = {}
        for speaker in speakers:
            speakers_map[speaker['id']] = speaker['speaker_name']
            
        
        transcripts = []
        speaker_id = None
        for item in transcript_data:
            if 'transcript' in item:
                if 'speaker_id' in item:
                    speaker_id = item['speaker_id']
                    speaker_name = speakers_map.get(speaker_id, 'Unknown Speaker')
                else:
                    speaker_id = None
                    speaker_name = 'Unknown Speaker'
                transcripts.append({'speaker_id':speaker_id,'speakers_name':speaker_name,'transcript': item['transcript']})
        
        data = {
            "speech_id": speech_id,
            "speech_title": speech_title,
            'summary':' '.join(speech_summary),
            "transcripts": transcripts
        }
        return JsonResponse(data, safe=False)
    except OtterAIException as e:
        return JsonResponse({"OtterAI Exception occurred": e}, safe=False)
    except Exception as e:
        return JsonResponse({"An unexpected error occurred": e},safe=False)