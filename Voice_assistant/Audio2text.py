import whisper
# import whisper
# print(whisper.__file__)
model = whisper.load_model("large")
text = model.transcribe(r"C:\\Users\Admin\Scripts\\Voice_assistant\\I will find YouI will Kill You Taken Movie best scene ever  liam neeson.mp4")
#printing the transcribe
text['text']