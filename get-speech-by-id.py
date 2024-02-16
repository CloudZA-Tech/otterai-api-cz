import json
from otterai import OtterAI, OtterAIException

def main():
    try:
        # Initialize
        otter = OtterAI()
        otter.login('', '')
        
        # found this to work to get the transcript alone from the data output when you use 'speech = otter.get_speech'
        speech_url = ""
        speech_index = ""
        speech = otter.get_speech(speech_index)
        speech_text = speech['data']
        speech_id = speech_text['speech']['speech_id']
        speech_title = speech_text['speech']['title']

        # Accessing the transcript data
        transcript_data = speech_text['speech']['transcripts'][0]['transcript']

        print("Speech Url:", speech_url)
        print("Speech ID:", speech_id)
        print("Speech Title:", speech_title)
        print("Transcript: ", transcript_data)
        print(speech)
        print("\n")

    except OtterAIException as e:
        print("OtterAI Exception occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()