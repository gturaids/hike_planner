##Lee Kamar
##Document converter
##2/09/2022

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
    #
    # allows us to change extension without changing the file name by removing appropriate num of letters
    # at the end of the file name
    # if doc_to_convert[-5:] == ".docx" or doc_to_convert[-5:] == ".html":
    #     change_extension=doc_to_convert[0:-5]
    #
    #
    # if doc_format=="1" and doc_to_convert[-5:] != ".docx":
    #     # try:
    #     wb=word.Documents.Open(input_file)
    #     #remove last 4 letters of file name
    #     output_file=os.path.abspath(change_extension + ".docx".format())
    #     wb.SaveAs2(output_file,FileFormat=16)
    #     print("Success! Converted document saved to the same directory as the original document")
    #     wb.Close()
    #
    #     # except:
    #     #     print("An error has occurred. Verify that you have entered the file name correctly and in the same directory as the program then retry")
    #
    #
    # elif doc_format=="2" and doc_to_convert[-4:] != ".txt":
    #     #try:
    #         wb=word.Documents.Open(input_file)
    #         #remove last 4 letters of file name
    #         output_file=os.path.abspath(change_extension + ".txt".format())
    #         wb.SaveAs2(output_file,FileFormat=4)
    #         print("Success! Converted document saved to the same directory as the original document")
    #         wb.Close()
    #
    #     #except:
    #         print("An error has occurred. Verify that you have entered the file name correctly and in the same directory as the program then retry")
    #
    # elif doc_format=="3" and doc_to_convert[-4:] != ".rtf":
    #     #try:
    #         wb=word.Documents.Open(input_file)
    #         #remove last 4 letters of file name
    #         output_file=os.path.abspath(change_extension + ".rtf".format())
    #         wb.SaveAs2(output_file,FileFormat=6)
    #         print("Success! Converted document saved to the same directory as the original document")
    #         wb.Close()
    #
    #     #except:
    #         print("An error has occurred. Verify that you have entered the file name correctly and in the same directory as the program then retry")
    #
    # elif doc_format=="4" and doc_to_convert[-5:] != ".html":
    #     #try:
    #         wb=word.Documents.Open(input_file)
    #         #remove last 4 letters of file name
    #         output_file=os.path.abspath(change_extension + ".html".format())
    #         wb.SaveAs2(output_file,FileFormat=10)
    #         print("Success! Converted document saved to the same directory as the original document")
    #         wb.Close()
    #
    #     #except:
    #         print("An error has occurred. Verify that you have entered the file name correctly and in the same directory as the program then retry")
    #
    # elif doc_format=="5" and doc_to_convert[-4:] != ".xps":
    #     #try:
    #         wb=word.Documents.Open(input_file)
    #         #remove last 4 letters of file name
    #         output_file=os.path.abspath(change_extension + ".xps".format())
    #         wb.SaveAs2(output_file,FileFormat=18)
    #         print("Success! Converted document saved to the same directory as the original document")
    #         wb.Close()
    #
    #     #except:
    #         print("An error has occurred. Verify that you have entered the file name correctly and in the same directory as the program then retry")
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

# maybe:
# while True: just check on the doc. if string == "True", then run weather loop which will overwrite the True value
# maybe do the open in read, close. the open in write, close instaed.