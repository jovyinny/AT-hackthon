import os
import time
import openai
import africastalking


openai.api_key = os.environ["openai_key"]
africastalking.initialize(os.environ["username"],os.environ["at_api_key"])
sms = africastalking.SMS


def send_sms(phone_number, message):
    shortcode=os.environ["shortcode"] # obtained from africas talking
    response = sms.send(message, [phone_number],shortcode)
    return response['SMSMessageData']['Recipients'][0]['status']


def get_chatgpt_response(message):
  # some prompt engineering here
  
  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=message,
      max_tokens=150,
      n=1,
      stop=None,
      temperature=0.5,
  )
  return response.choices[0].text.strip()



def fetch_last_message_id():
    last_received_id = 0
    while True:
        message_data = sms.fetch_messages(last_received_id=last_received_id)
        messages = message_data['SMSMessageData']['Messages']
        if len(messages) == 0:
            break
        for message in messages:
            last_received_id = message['id']
    return last_received_id
  

def main():
    last_message_id = fetch_last_message_id()
  
    while True:
        message_data = sms.fetch_messages(last_received_id=last_message_id)
        messages = message_data['SMSMessageData']['Messages']
        
        for message in messages:
            
            message_text = message['text']
            phone_number=message["from"]
          
            chatgpt_response = get_chatgpt_response(message_text)
            send_sms(phone_number, chatgpt_response)
            print(f"message sent {phone_number}")

            last_message_id = message['id']
        time.sleep(2)
      

if __name__ == "__main__":
    main()
