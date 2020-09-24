

from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/mac/Desktop/key/Moockt-STT-f2ea661c8c81.json"

def sample_long_running_recognize(storage_uri):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1.SpeechClient()

    # storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw'

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # The language of the supplied audio
    language_code = "ko-KR"

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    # encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": 'FLAC',
        "audio_channel_count":2,
        "enable_word_time_offsets": True,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
        for word in alternative.words:
            print(u"Word: {}".format(word.word))
            
            print(
                u"Start time: {} seconds {} nanos".format(
                    word.start_time.seconds, word.start_time.nanos
                )
            )
            print(
                u"End time: {} seconds {} nanos".format(
                    word.end_time.seconds, word.end_time.nanos
                )
            )
    # The first result includes start and end time word offsets

    # result = response.results[0]
    # # First alternative is the most probable result
    # alternative = result.alternatives[0]
    # print(u"Transcript: {}".format(alternative.transcript))
    # # Print the start and end time of each word
    # for word in alternative.words:
    #     print(u"Word: {}".format(word.word))
    #     print(
    #         u"Start time: {} seconds {} nanos".format(
    #             word.start_time.seconds, word.start_time.nanos
    #         )
    #     )
    #     print(
    #         u"End time: {} seconds {} nanos".format(
    #             word.end_time.seconds, word.end_time.nanos
    #         )
    #     )

storage_uri = 'gs://moockt/operating-system-8-1.flac'

sample_long_running_recognize(storage_uri)