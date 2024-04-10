import openai
import azure.cognitiveservices.speech as speechsdk
import pyttsx3




def recognize_from_microphone(speech_key, speech_region):
    # Define and assign the Speech API key and region
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    speech_config.speech_recognition_language = "en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

# Set your OpenAI API key

# Example usage:
speech_key = "51ea1f1487cb413eb0ed452817ed6ef7"
speech_region = "japaneast"

spoken_text = recognize_from_microphone(speech_key, speech_region)
print("Recognized: {}".format(spoken_text))

# Language Analysis with OpenAI
response = openai.chat.completions.create(
    engine="davinci-codex",
    prompt="Correct the following text: " + spoken_text,
    max_tokens=100
)

corrected_text = response['choices'][0]['text'].strip()
print("Corrected Text: {}".format(corrected_text))

# Text-to-Speech
engine = pyttsx3.init()
engine.say(corrected_text)
engine.runAndWait()
