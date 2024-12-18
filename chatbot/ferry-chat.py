from openai import OpenAI

client = OpenAI(api_key='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')

while True:
    # Get user input


    user_input = input("You: ")

    with open('./clean-data/sample-schedule.txt') as file:
        ferry_schedule = file.read()

    with open('./clean-data/travel-and-safety-information.txt') as file:
        travel_and_safety = file.read()

    with open('./clean-data/ferry-history.txt') as file:
        ferry_history = file.read()

    if user_input.lower() == "exit":
        print("Goodbye!")
        break


    # Make a request to the OpenAI API
    response = client.chat.completions.create(model="gpt-3.5-turbo",  # Use "gpt-4" or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant that is knowledgeable about the guemes island ferry. You use nautical references whenver possible."},
        {"role": "system", "content": ferry_schedule},
        {"role": "system", "content": travel_and_safety},
        {"role": "system", "content": ferry_history},
        {"role": "user", "content": user_input}
    ])

    # Extract and print the assistant's response
    assistant_response = response.choices[0].message.content
    print(assistant_response)