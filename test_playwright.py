from playwright.sync_api import sync_playwright
# 上海悠悠 wx:283340479
# blog:https://www.cnblogs.com/yoyoketang/


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()  # 创建上下文，浏览器实例1

    page = context.new_page()    # 打开标签页
    page.goto("https://www.baidu.com/")
    print(page.title())
    page.screenshot(path="screenshot.png")
