from pyreveal import PyReveal, ImageBackground

# 相對路徑或絕對路徑都可以
bg_image_path = "assets/blockhole.jpg"

presentation = PyReveal(title="My Presentation", theme="white", transition="slide")
bg_image = ImageBackground(image_url=bg_image_path)

# 加入幻燈片
presentation.add_slide(
    title="第8組報告",
    content="成員:6、7、12、13、19、42",
    background=bg_image
)
presentation.add_slide(
    title="什麼是 Git？",
    content="""
- 分散式版本控制系統
- 可追蹤檔案變化
- 協作工具
""",
    background=bg_image
)

presentation.add_slide("""如何使用 Git？
1. git init 建立版本庫
2. git add 加入檔案
3. git commit 提交版本
4. git push 上傳到遠端
""", background=bg_image)
presentation.add_slide("""為什麼要用 Git？
- 團隊合作方便
- 保留歷史紀錄
- 可回溯版本
""", background=bg_image)
presentation.add_slide("1234", background=bg_image)
presentation.add_slide("1234", background=bg_image)
presentation.add_slide("謝謝大家", background=bg_image)

# 生成 HTML 簡報
presentation.save_to_file("my_presentation.html")
print("簡報生成完成！")
 
