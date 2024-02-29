from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2
import numpy as np
from PyQt5.QtCore import QCoreApplication


from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from pygtrans import Translate # 英轉中
from zhconv import convert # 簡轉繁
import pyttsx3
import openai

from UI import Ui_MainWindow

all_img_path = [0,0,0]

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # ToDo
        self.ui.download.setEnabled(False)
        self.ui.speaker.setEnabled(False)

        self.ui.select_img_1.clicked.connect(self.image_1)
        self.ui.select_img_2.clicked.connect(self.image_2)
        self.ui.select_img_3.clicked.connect(self.image_3)

        self.ui.style_happy.clicked.connect(self.style_happy)
        self.ui.style_horror.clicked.connect(self.style_horror)
        self.ui.style_sad.clicked.connect(self.style_sad)
        self.ui.style_heatwarming.clicked.connect(self.style_heatwarming)

        self.ui.download.clicked.connect(self.save_story)
        self.ui.speaker.clicked.connect(self.tell_story)
        self.ui.delete_2.clicked.connect(self.clearData)


    def image_1(self):
        img_path, filetype = QFileDialog.getOpenFileName(self)
        
        if img_path:
            global all_img_path
            all_img_path[0] = img_path
            # img_path_split = img_path.split("/")
            # pathSize = len(img_path_split)
            # imgPath = img_path_split[pathSize-1]

            img=cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),-1)

            if (img.shape[0] > 270) or (img.shape[1] > 360):
                if img.shape[0] > 270:
                    img = cv2.resize(img, (img.shape[1], 270))
                
                if img.shape[1] > 360:
                    img = cv2.resize(img, (360, img.shape[0]))

            height, width, channel = img.shape
            bytesPerline = 3 * width
            qimg = QImage(img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
            self.ui.Image1.setPixmap(QPixmap.fromImage(qimg))

    def image_2(self):
        img_path, filetype = QFileDialog.getOpenFileName(self)
        
        if img_path:
            global all_img_path
            all_img_path[1] = img_path
            img=cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),-1)

            if (img.shape[0] > 270) or (img.shape[1] > 360):
                if img.shape[0] > 270:
                    img = cv2.resize(img, (img.shape[1], 270))
                
                if img.shape[1] > 360:
                    img = cv2.resize(img, (360, img.shape[0]))

            height, width, channel = img.shape
            bytesPerline = 3 * width
            qimg = QImage(img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
            self.ui.Image2.setPixmap(QPixmap.fromImage(qimg))

    def image_3(self):
        img_path, filetype = QFileDialog.getOpenFileName(self)
        
        if img_path:
            global all_img_path
            all_img_path[2] = img_path
            img=cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),-1)

            if (img.shape[0] > 270) or (img.shape[1] > 360):
                if img.shape[0] > 270:
                    img = cv2.resize(img, (img.shape[1], 270))
                
                if img.shape[1] > 360:
                    img = cv2.resize(img, (360, img.shape[0]))

            height, width, channel = img.shape
            bytesPerline = 3 * width
            qimg = QImage(img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
            self.ui.Image3.setPixmap(QPixmap.fromImage(qimg))

    # 根據影像產生說明句


    def get_img_sentance(self):
        model_path = "./BlipModel/"
        # model = BlipForConditionalGeneration.from_pretrained(model_path)
        # processor = BlipProcessor.from_pretrained(model_path)

        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

        client = Translate()
        all_ch_outSen = []
        # 開始讀取圖片
        global all_img_path
        for p in all_img_path:
            raw_img = Image.open(p)
            inputs = processor(raw_img, return_tensors="pt")
            out = model.generate(**inputs)
            en_outSen = processor.decode(out[0], skip_special_tokens=True) # 轉簡體
            ch_outSen = convert(client.translate(en_outSen).translatedText, 'zh-tw') # 英轉中 -> 簡轉繁
            all_ch_outSen.append(ch_outSen)
            print(ch_outSen)
        return all_ch_outSen

    

    def text2story(self, styleMode):
        openai.api_key = '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' # 設定API金鑰
        all_ch_outSen = self.get_img_sentance()
        # 使用GPT-3模型進行互動
        styles = ['快樂', '恐怖', '悲傷', '勵志'] 

        p4 = "生成一個" + styles[styleMode] + "的中文故事" # UI? 使用者選擇style

        prompts = [all_ch_outSen[0] , all_ch_outSen[1] , all_ch_outSen[2] , p4]
        prompt = "||".join(prompts)  # 將多個prompt組合成一個長的文本串，使用"||"分隔


        response = openai.Completion.create(
            engine = "text-davinci-003",  # 或其他可用的GPT-3引擎
            # davinci:最強大的GPT-3模型引擎，用於處理複雜和多樣化的任務。
            # curie:較小型的GPT-3模型引擎，適用於大多數一般任務和用例。
            prompt = prompt,
            max_tokens = 2000 # 控制生成文本長度的參數 ( https://platform.openai.com/tokenizer )
        )
        
        print("prompt : ", prompt)
        story = response.choices[0].text.strip()
        return story
        # print(story)

    def style_happy(self):

        
        self.ui.style_happy.setStyleSheet('''QPushButton{background:#0080FF;border-radius:5px;}''')
        self.ui.style_horror.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_sad.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_heatwarming.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        
        self.ui.show_story.setText("故事產出中，請稍後")
        QCoreApplication.processEvents()
        
        if all_img_path[0] != 0 and all_img_path[1] != 0 and all_img_path[2] != 0:
            
            self.ui.style_heatwarming.setEnabled(False)
            self.ui.style_horror.setEnabled(False)
            self.ui.style_sad.setEnabled(False)

            story = self.text2story(0)
            self.ui.show_story.setText(story)
            self.ui.download.setEnabled(True)
            self.ui.speaker.setEnabled(True)
        
        else:
            self.ui.show_story.setText("請選滿3張圖片")


    def style_horror(self):
        self.ui.style_horror.setStyleSheet('''QPushButton{background:#0080FF;border-radius:5px;}''')
        self.ui.style_happy.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_sad.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_heatwarming.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')

        self.ui.show_story.setText("故事產出中，請稍後")
        QCoreApplication.processEvents()
        
        if all_img_path[0] != 0 and all_img_path[1] != 0 and all_img_path[2] != 0:
            
            self.ui.style_heatwarming.setEnabled(False)
            self.ui.style_happy.setEnabled(False)
            self.ui.style_sad.setEnabled(False)

            story = self.text2story(1)
            self.ui.show_story.setText(story)
            self.ui.download.setEnabled(True)
            self.ui.speaker.setEnabled(True)
        
        else:
            self.ui.show_story.setText("請選滿3張圖片")

    def style_sad(self):
        self.ui.style_sad.setStyleSheet('''QPushButton{background:#0080FF;border-radius:5px;}''')
        self.ui.style_happy.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_horror.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_heatwarming.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')

        self.ui.show_story.setText("故事產出中，請稍後")
        QCoreApplication.processEvents()
        
        if all_img_path[0] != 0 and all_img_path[1] != 0 and all_img_path[2] != 0:
            
            self.ui.style_heatwarming.setEnabled(False)
            self.ui.style_horror.setEnabled(False)
            self.ui.style_happy.setEnabled(False)

            story = self.text2story(2)
            self.ui.show_story.setText(story)
            self.ui.download.setEnabled(True)
            self.ui.speaker.setEnabled(True)
        
        else:
            self.ui.show_story.setText("請選滿3張圖片")


    def style_heatwarming(self):
        self.ui.style_heatwarming.setStyleSheet('''QPushButton{background:#0080FF;border-radius:5px;}''')
        self.ui.style_happy.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_horror.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_sad.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        
        self.ui.show_story.setText("故事產出中，請稍後")
        QCoreApplication.processEvents()

        if all_img_path[0] != 0 and all_img_path[1] != 0 and all_img_path[2] != 0:
            self.ui.style_happy.setEnabled(False)
            self.ui.style_horror.setEnabled(False)
            self.ui.style_sad.setEnabled(False)
            
            # global story
            story = self.text2story(3)
            self.ui.show_story.setText(story)
            self.ui.download.setEnabled(True)
            self.ui.speaker.setEnabled(True)

        else:
            self.ui.show_story.setText("請選滿3張圖片")


    def tell_story(self):
        # global story
        story = self.ui.show_story.toPlainText()

        if len(story)!=0:
            story = self.ui.show_story.toPlainText()
            print(story)

            # 文字轉語音
            engine = pyttsx3.init()
            engine.setProperty('voice', 'zh')
            # engine.setProperty('rate', 170) # 語速設定

            engine.say(story) # 開始播放語音
            engine.save_to_file(story, "./story.mp3") # 音檔輸出
            engine.runAndWait()

    def save_story(self):
        # 儲存故事內容為txt，以寫入模式（'w'）創建或覆寫文件
        story = self.ui.show_story.toPlainText()
        if len(story)!=0:
            print(story)
            with open("./story.txt", "w", encoding="utf-8") as file:
                file.write(story)
    
    def clearData(self):
        self.ui.show_story.setText("")

        self.ui.Image1.setText("[None]")
        self.ui.Image2.setText("[None]")
        self.ui.Image3.setText("[None]")

        self.ui.style_happy.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_horror.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_sad.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')
        self.ui.style_heatwarming.setStyleSheet('''QPushButton{background:#FFFFFF;border-radius:5px;border:1px solid rgb(209, 209, 209);}''')

        self.ui.style_happy.setEnabled(True)
        self.ui.style_heatwarming.setEnabled(True)
        self.ui.style_horror.setEnabled(True)
        self.ui.style_sad.setEnabled(True)

        self.ui.download.setEnabled(False)
        self.ui.speaker.setEnabled(False)

        global all_img_path
        all_img_path[0] = 0
        all_img_path[1] = 0
        all_img_path[2] = 0
        
        