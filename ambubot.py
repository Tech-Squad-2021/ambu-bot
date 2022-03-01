def send_msg(sender_number, reciever_number, message):
    client.messages.create(
        to=reciever_number,
        from_=sender_number,
        body=message,
    )
    return ('', 200)


@app.route('/', methods=['POST'])
def AmbuBot():

    sender_number = request.form['From']
    reciever_number = request.form['To']
    msg_body = request.form['Body']

    print(msg_body)

    if msg_body == 'hi':
        send_msg(reciever_number, sender_number, intro)

    if msg_body == "1":
        send_msg(reciever_number, sender_number, 'Location?')
        print(msg_body, 'OK')

        # data = scrapper.getData(3, "Kolkata")
        # send_msg(reciever_number, sender_number, str(data))

    return ('', 200)


if __name__ == '__main__':
    app.run()
