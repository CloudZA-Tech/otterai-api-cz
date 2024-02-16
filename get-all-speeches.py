import json
from otterai import OtterAI, OtterAIException

def main():
    try:
        # Initialize
        otter = OtterAI()
        otter.login('', '')
        
        # found this to work to get the transcript alone from the data output when you use 'speech = otter.get_speech'
        speech = otter.get_speeches()
        speech_data = speech['data']
        print(speech_data)

    except OtterAIException as e:
        print("OtterAI Exception occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()