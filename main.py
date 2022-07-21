import textwrap
from PIL import Image, ImageDraw, ImageFont


question = input("Enter the Question : ")
option_1 = input("Enter the first option : ")
option_2 = input("Enter the second option : ")
option_3 = input("Enter the third option : ")
option_4 = input("Enter the fourth option : ")

imageObject = Image.open("image.jpeg")

font_Object = ImageFont.truetype('C:\\Users\\bnaya\\PycharmProjects\\Pilllow Automation\\Cabin_Condensed\\CabinCondensed-Regular.ttf', 48)
option_font = ImageFont.truetype('C:\\Users\\bnaya\\PycharmProjects\\Pilllow Automation\\Cabin_Condensed\\CabinCondensed-Regular.ttf', 23)
header_font = ImageFont.truetype('C:\\Users\\bnaya\\PycharmProjects\\Pilllow Automation\\Cabin_Condensed\\CabinCondensed-Bold.ttf', 55)
footer_font = ImageFont.truetype('C:\\Users\\bnaya\\PycharmProjects\\Pilllow Automation\\Cabin_Condensed\\CabinCondensed-Regular.ttf', 21)

drawingObject = ImageDraw.Draw(imageObject)

header = "QUIZ TIME !"
footer = "@technologychannel.org"
drawingObject.text((500, 6), f"{header}", fill=(245, 235, 255), font=header_font)

wrapper = textwrap.TextWrapper(width=55)
word_list = wrapper.wrap(text=question)
caption_new = ''
for ii in word_list[:-1]:
    caption_new = caption_new + ii + '\n'
caption_new += word_list[-1]

drawingObject.text((119, 96), f"{caption_new}", fill=(245, 235, 255), font=font_Object)
drawingObject.text((142, 308), f"{option_1}", fill=(252, 252, 252), font=option_font)
drawingObject.text((138, 407), f"{option_2}", fill=(252, 252, 252), font=option_font)
drawingObject.text((138, 503), f"{option_3}", fill=(252, 252, 252), font=option_font)
drawingObject.text((136, 602), f"{option_4}", fill=(252, 252, 252), font=option_font)
drawingObject.text((520, 675), f"{footer}", fill=(245, 235, 255), font=footer_font)


imageObject.save('newimage.jpeg', quality=95)

