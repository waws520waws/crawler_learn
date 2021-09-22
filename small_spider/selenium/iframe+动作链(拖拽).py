from selenium import webdriver
import time
from selenium.webdriver import ActionChains

# webdri = webdriver.Chrome(executable_path='./chromedriver.exe')
webdri = webdriver.Firefox(executable_path='./geckodriver.exe')

webdri.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 切换到iframe的作用域（参数要唯一）
webdri.switch_to.frame('iframeResult')
# 切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档。
# webdri.switch_to.default_content()
# 从子frame切回到父frame，而不用我们切回主文档再切进来
# webdri.switch_to.parent_frame()  # 如果当前已是主文档，则无效果

# 然后在此iframe中定位元素（参数要唯一）
drag = webdri.find_element_by_id('draggable')

print(type(drag))
print(drag.text)

# 实例化动作链对象
action = ActionChains(webdri)

action.click_and_hold(drag)

for i in range(5):
    # perform立即执行动作链操作
    action.move_by_offset(17, 0).perform()

# 释放动作链
action.release()