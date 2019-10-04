import os
import time

from pathlib import Path
from constant import constant

key_code = " -vcodec copy -acodec copy -encryption_scheme cenc-aes-ctr -encryption_key 76a6c65c5ea762046bd749a2e632ccbb -encryption_kid a7e61c373e219033c21091fa607bf3b8 "
out_forder = "C:\\Work\\media\\encrypted"
# file_path = "C:\\Work\\test project\\github\\mysite\\media\\out2019-10-04T132602.avi"
file_path2 = "C:\\Work\\media\\out2019-10-04T132602.avi"
os.system("ffmpeg.exe -i " + file_path2 + key_code + out_forder + "encrypted{}.mp4".format(file_path2[-24:-4]))


# ffplay encFile_name -decryption_key 76a6c65c5ea762046bd749a2e632ccbb
# time.sleep()
time.sleep(5)
decryption_file_name = "C:\\Work\\media\\encryptedencryptedout2019-10-04T132602.mp4"
os.system("ffplay {} -decryption_key 76a6c65c5ea762046bd749a2e632ccbb".format(decryption_file_name))