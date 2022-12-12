from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import shuffle
def createimg(kasbnomi,kasbnarxi,kompaniya):
    imgList = ['creatorimg/img/img1.jpg', 'creatorimg/img/img2.jpg', 'creatorimg/img/img3.jpg', 'creatorimg/img/img4.jpg']
    shuffle(imgList)

    img1 = Image.open('creatorimg/template.jpg')
    img2 = Image.open(imgList[0])


    mask = Image.new('L', img2.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((20,1,280,270), fill=255)

    img1.paste(img2, (250, 480), mask)
    # Call draw Method to add 2D graphics in an image


    I1 = ImageDraw.Draw(img1)

    jobName = kasbnomi
    jobPrice = kasbnarxi
    companyName = kompaniya

    jobNameFont = ImageFont.truetype('creatorimg/Neue.ttf', 100)
    jobPriceFont = ImageFont.truetype('creatorimg/Neue.ttf', 115)
    companyNameFont = ImageFont.truetype('creatorimg/Neue.ttf', 60)

    # Add Text to an image
    I1.text((600, 470), jobName, font=jobNameFont, fill =('white'))
    I1.text((600, 650), f"{jobPrice}", font=jobPriceFont, fill =('springgreen'))
    I1.text((300, 938), companyName, font=companyNameFont, fill =('white'))

    # Display edited image
    # img1.show()

    # Save the edited image
    img1.save("creatorimg/result.png", format='png')
    return True
