import mailbox
from flask import Flask, request, render_template
from imap_tools import MailBox, AND, OR, A


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def my_form_post():    
        global username
        username= request.form['username']
        global password
        password=request.form['password']
       
 
    # Get date, subject and body len of all emails from INBOX folder
        with MailBox('imap.gmail.com').login(username, password, 'Inbox') as mailbox:
         for msg in mailbox.fetch():
            print(username,password)
            text = request.form['text']
            processed_text = text
            msg.subject
            from_email = A(text=[processed_text])
            fetch_email = [msg.subject for msg in mailbox.fetch(from_email)]
            #move_email = mailbox.move([msg.subject for msg in mailbox.fetch('TEXT "Badge"')], 'Notes')
            email_length = len(fetch_email)
             
            return render_template('index.html',  processed_text=processed_text, b=fetch_email, email_length=email_length, username=username,password=password)    
    

if __name__ == '__main__':
    app.run()