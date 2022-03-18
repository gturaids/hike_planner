# This is the microservices provided by my teammate, Lee Kamar, and edited to remove features not used by my app.
# Document converter
# 2/09/2022

import os
import win32com.client
import time

word = win32com.client.Dispatch("word.Application")
word.visible = 0


def loop():
    while True:
        time.sleep(1)
        print("Waiting for request")
        with open("converter.txt", 'r+') as incoming_signal:
            convert = incoming_signal.read()
            if convert == "True":
                incoming_signal.write("False")
                doc_to_convert = "hike_list.txt"
                doc_format = "6"
                input_file = os.path.abspath(doc_to_convert)
                change_extension = doc_to_convert[0:-4]

                if doc_format == "6" and doc_to_convert[-4:] != ".pdf":  # elif in full program
                    try:
                        wb = word.Documents.Open(input_file)
                        #remove last 4 letters of file name
                        output_file = os.path.abspath(change_extension + ".pdf".format())
                        wb.SaveAs2(output_file, FileFormat=17)
                        print("Success! Converted document saved to the same directory as the original document")
                        wb.Close()
                        break # weather_loop()

                    except:
                        print("An error has occurred. Verify that you have entered the file name correctly and in the same directory as the program then retry")

                else:
                    print("Error: Document conversion has to be to a different file format. Retry")


loop()

