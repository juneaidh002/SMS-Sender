from twilio.rest import Client

# Twilio account SID and authentication token
account_sid = "AC0a16a91b48cf9bca93e092911322d1a2"
auth_token = "3b7160e8e0d98f120582c3cbb1be959f"
twilio_phone_number = "+14846236375"

def send_sms(phone_number, message):
    try:
        # Create a Twilio client
        client = Client(account_sid, auth_token)
        
        # Send the SMS message
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=phone_number
        )

        # Display a confirmation message
        print("Message sent successfully!")
        print("Message SID:", message.sid)
        
    except Exception as e:
        # Handle any exceptions or errors
        print("An error occurred while sending the message:", str(e))


def main():
    # Prompt the user to enter their phone number
    phone_number = input("Enter your phone number (including country code): ")

    # Validate the phone number format
    # You can implement your own validation logic here

    # Prompt the user to enter the message
    message = input("Enter the message you want to send: ")

    # Send the SMS
    send_sms(phone_number, message)


if __name__ == "__main__":
    main()
