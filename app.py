from cgitb import text
from crypt import methods
from ctypes.wintypes import MSG
from plistlib import UID
from urllib.request import urlopen
from flask import Flask, request, render_template, url_for, redirect
from imap_tools import MailBox, AND, OR, A
from requests import post
from flask_paginate import Pagination, get_page_parameter



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template ('login.html')

@app.route('/', methods=['GET','POST'])
def my_form_post():    
        global username
        username= request.form['username']
        global password
        password=request.form['password']   
   
 
    # Get date, subject and body len of all emails from INBOX folder
        with MailBox('imap.gmail.com').login(username, password, 'Inbox') as mailbox:
           
            #move_email = mailbox.move([msg.subject for msg in mailbox.fetch('TEXT "Badge"')], 'Notes')if request.method == 'POST':
            return render_template('index.html', username=username,password=password)   

@app.route('/first')
def my_for1():
    return render_template('index.html') 

@app.route('/first', methods=['GET','POST'])
def my_first_post():    
        global from_email 
        from_email = text = request.form['text']
        
      
    # Get date, subject and body len of all emails from INBOX folder
      
        
        with MailBox('imap.gmail.com').login(username, password, 'Inbox') as mailbox:
         for msg in mailbox.fetch():
            text = text = request.form['text']
            processed_text = text   
            msg.subject
            from_email = A(text=[processed_text])
            fetch_email = [msg.from_ for msg in mailbox.fetch(from_email)]
            #move_email = mailbox.move([msg.subject for msg in mailbox.fetch('TEXT "Badge"')], 'Notes')
            email_length = len(fetch_email)
            
           # if email_length != 0:
               # move_email = mailbox.move([msg.uid for msg in mailbox.fetch(from_email)], 'Inbox')
            return render_template ('index.html',  processed_text=processed_text, b=fetch_email, email_length=email_length, username=username)    

@app.route('/delete')
def my_form_del():
    return render_template ('index.html')

@app.route('/delete', methods=['GET','POST'])
    
def my_form_dele():
   
    with MailBox('imap.gmail.com').login(username, password, 'Inbox') as mailbox:  
             move_email = mailbox.move([msg.uid for msg in mailbox.fetch(from_email)], '[Gmail]/Trash')
             return render_template ('index.html', move_email=move_email)
    
