#!/bin/python
#!/bin/python3
import tkinter,time,webview,os

tewi = tkinter.Tk()

tewi.geometry("600x400")
tewi.overrideredirect(True)

l = tkinter.Label(tewi, text="We hope you enjoyed the Beta test of our app. See you again later!", font="Roboto")
b = tkinter.Button(tewi, text="Cancel", command=tewi.destroy, font="Roboto")
l.pack()
b.pack()
webview.create_window('RapidChat', 'https://rapidchat.ericplayzyt.repl.co')
webview.start()


print("By turning on WebView, you agree to the terms and conditions of our website.")
tewi.mainloop()
