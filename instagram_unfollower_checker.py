import moviepy.editor as mp

# مسیر فایل ویدیوی ورودی
input_video = "Media1.mp4"

# بارگذاری ویدیو
video = mp.VideoFileClip(input_video)

# زمان شروع و پایان بخش قابل حذف
start_cut = 2
end_cut = 11

# برش ویدیو به دو قسمت
part1 = video.subclip(0, start_cut)
part2 = video.subclip(end_cut, video.duration)

# ترکیب دو بخش
final_video = mp.concatenate_videoclips([part1, part2])

# خروجی فایل
output_video = "output_video.mp4"
final_video.write_videofile(output_video, codec="libx264", audio_codec="aac")

print("ویدیو با موفقیت ساخته شد!")
