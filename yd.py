from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *
font = ('verdana', 20)
file_size = 0


# oncomplete callback function
def completeDownload(stream=None, file_path=None):
    print("download completed")
    showinfo("Message", "File has been downloaded...")
    downloadBtn['text'] = "Download Video"
    downloadBtn['state'] = "active"
    urlField.delete(0, END)


# onprogress callbackfunction
def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    downloadBtn['text'] = "{:00.0f}% downloaded ".format(percent)


# download function
def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        yt = YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save)

    except Exception as e:
        print(e)
        print("something went wrong")


def btnClicked():
    try:
        downloadBtn['text'] = "Please wait..."
        downloadBtn['state'] = 'disabled'
        url = urlField.get()
        if url == '':
            return
        print(url)
        thread = Thread(target=startDownload, args=(url,))
        thread.start()

    except Exception as e:
        print(e)


# gui coding
root = Tk()
root.title("python life Youtube downloader")

root.geometry("500x600")

# main icon section


# making url field
urlField = Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
urlField.focus()
# download btn
downloadBtn = Button(root, text="Download Video", font=font, relief='ridge', command=btnClicked)
downloadBtn.pack(side=TOP, pady=20)

root.mainloop()
