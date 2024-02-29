# 看圖聯想有聲書

## :small_blue_diamond:Introduction

現在家庭多為雙薪家庭，父母很難有太多時間陪伴孩子，就算回到家也很難有多餘的精力與孩子互動。因此製作了一個「看圖聯想有聲書」的應用，透過輸入多張圖片，生成一段具有連續性的故事，且能夠根據使用者需求選擇故事的情感走向來決定故事風格。最後透過 text-to-speech 的技術，將故事轉為有聲書。

* 使用對象:
    - 協助想不到故事的父母，作為安撫孩子的應用
    - 讓孩子能夠創意搭配圖片，嘗試產生屬於自己的有聲書


## :small_blue_diamond:Method
![](https://github.com/jaifenny/Audiobook/blob/main/picture/1.png)

### Step 1 : Image to text
* 輸出影像對應的描述短句
* 使用模型 : BLIP
    * 提出 CapFilt 數據集增強，提升訓練資料品質，增加模型在image captoning任務上的能力

### Step 2 : Sentence to story
* 將圖片產生的短文描述(p1 ~ p3)，加上指定的故事風格(p4)，作為 prompt (p1 ~ p4)餵給大型語言模型，以獲得完整故事內容。
* 模型 : GPT-3.5
```
styles = ['快樂', '恐怖', '悲傷', '溫馨'] 
p4 = "生成一個" + styles[0] + "的中文故事" 
prompts = [
    p1 , p2 , p3 , p4
]
prompt = "||".join(prompts)
```

### Step 3 : Story to voice
* Text to speech(TTS) 任務，將文字內容轉為語音輸出
* 套件 : pyttsx3

### Step 4 : UI interface
* 功能 : 
    * 圖片上傳 : 讓使用者上傳任意圖片，作為故事生成的主軸
    * 故事風格 : 提供四種可選擇的劇情風格，「快樂」、「恐怖」、「悲傷」、「勵志」
    * 講故事 :  將產生的文字故事以語音播出
    * 匯出故事 : 將生成的故事以txt、語音以mp3格式匯出，存在指定位置

## :small_blue_diamond:Results

![](https://github.com/jaifenny/Audiobook/blob/main/picture/2.png)


## :small_orange_diamond:Discussion

- 影像描述的精度取捨 : BLIP 模型是基於現實生活中的靜態影像所訓練而成，因此對於繪圖的文字生成會較為失真。且因考量到設備需求要求，故選用小型的 base 規格模型，以部分精確度換取較短的運行時間及設備需求。 
- Prompt engineering : 在影像間關聯性本身就較差，或是圖片轉文字時產生的描述過於詳細時，GPT-3.5 會為了盡量符合描述而容易出現不合理的文字描述，因此未來需要實驗尋找更加精確的指令，同時也須搭配長度控制的指令以及搭配生成時參數的設置調整，以避免產生不合理劇情或過於冗長的故事文字。

## :small_orange_diamond:Conclusion

- 「看圖聯想有聲書」能夠讓使用者輸入三張影像以及選擇故事風格，以產出豐富有趣的故事劇情，能夠協助忙碌的父母作為講故事的保母，孩子也能發揮自己的想像力去拼湊屬於自己的故事。同時「看圖聯想有聲書」能夠透過 CPU 運行，並且在可接受的時間內獲得輸出。
- 雖然目前在少數故事內容合理性上還有待加強，但未來將會透過加入繪畫影像搭配描述文字來微調 BLIP 模型，以增加對於圖像的描述能力，並且也將在 prompt engineering 部分進行實驗，找出最能夠精準發揮 GPT-3.5 模型能力的指令。

