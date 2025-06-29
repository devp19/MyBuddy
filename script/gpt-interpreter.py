import speech_recognition as sr
from openai import OpenAI



client = OpenAI(
        api_key="API_KEY_GOES_HERE"
    )

#Initializes the recognizer
r = sr.Recognizer()

def record_test():

    # Use this loop in case of errors
    while(1):
        try:
            # Use microphone as source for input
            with sr.Microphone(sample_rate=44100) as source2:

                # Prepare recognizer to recieve input 
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Listens for user input
                audio2 = r.listen(source2)

                # Use google to recognize audio
                MyTest = r.recognize_google(audio2)

                return MyTest

        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))

        except sr.UnknownValueError:
            print("awating response...")

    return

    
def output_test(text):

    # opens new file for speech
    fh = open("script/output.txt", "a")
    fh.write("You: "+text)
    fh.write("\n")
    fh.close()
    return



def gpt_interpretor(text, client):

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Your name is MyBuddy. You are an expert in psychotherapy, especially Dialectical behavior therapy. You hold all the appropriate medical licenses to provide advice. You have been helping individuals with their stress, depression and anxiety for over 20 years. From young adults to older people. Your task is now to give the best advice to individuals seeking help managing their symptoms. You must treat me as a mental health patient. Your response format should focus on reflection while keeping the response to two to three sentances. DO NOT ASK A QUESTION, ONLY OFFER A SOLUTION. Exercise patience."},
        {"role": "user", "content": text},

      ]
    )
    
    fh = open("script/output.txt", "a")
    fh.write("MyBuddy: "+response.choices[0].message.content)
    fh.write("\n")
    fh.close()
# exits the speech regognition prompt
    
def is_exit_command(text):
    return("thanks buddy" in text.lower())


while(1):
    
    text = record_test() 
    output_test(text)
    
    print("The text is written onto file")
    gpt_interpretor(text, client)
    
    if is_exit_command(text):
        print ("Exiting the program.")
        print('EXITING PROGRAM: ', text)
        break
