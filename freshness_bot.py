import telebot
import detect

bot = telebot.TeleBot('1761476605:AAFg4THBdwKg2cz3bGMUg9U-8kpEmsPEZd4')

@bot.message_handler(content_types=['photo'])
def handle(message):

   # DownloadFile(message.Photo[message.Photo.Length - 1].FileId, @ "c:\photo.jpg")

    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)

    downloaded_file = bot.download_file(file_info.file_path)
    src = r'C:\home\artem_kug\freshness\images\\' + message.photo[1].file_id + '.jpg'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    opt = {'weights': 'runs/train/exp/new.pt', 'source': 'images', 'img_size': 640,
    'conf_thres':0.25, 'iou_thres': 0.45, 'device':'', 'view_img': False,
    'save_txt': False, 'save_conf': False, 'nosave': False, 'classes': None,
    'agnostic_nms': False, 'augment': False, 'update': False, 'project': r'runs/detect',
    'name': 'exp', 'exist_ok': False}
    detect.detect(opt)
    bot.send_photo(message.chat.id, open('runs\detect\exp\\' + message.photo[1].file_id + '.jpg', 'rb'))
    #bot.reply_to(message, "Фото добавлено")

    #bot.send_photo(message.chat.id, open(r'C:\home\artem_kug\image', 'rb'))

bot.polling(none_stop=True, interval=1)
# #extract the image name for further operations
#     image_name = save_image_from_message(message)
# # execute object recognition
#     object_recognition_image(image_name)
# # send object recognition results
#     bot.send_photo(message.chat.id, open('.data/darknet/predictions.jpg’,’rb’), ‘Identified objects')
# # execute image classification
#     classification_list_result = classify_image(image_name)
# # send classification results
#     output = 'The image classifies as:\n'
#     for result in classification_list_result:
#         output += result
#         output += '\n🚀 Gimme more pics! 🚀'
#     bot.reply_to(message, output)
# # remove picture from server
#     cleanup_remove_image(image_name);