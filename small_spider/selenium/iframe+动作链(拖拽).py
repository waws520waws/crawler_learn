from selenium import webdriver
import time
from selenium.webdriver import ActionChains

webdri = webdriver.Chrome('D:/pyEnvsPackage/chromedriver_win32_92/chromedriver.exe')
# webdri = webdriver.Firefox(executable_path='./geckodriver.exe')

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
print(drag.location)

## 实例化动作链对象
action = ActionChains(webdri)

# 模拟人移动鼠标到指定DOM元素位置
action.move_to_element(drag).perform()

action.click_and_hold(drag).perform()

for i in range(5):
    ## 当调用ActionChains的方法时，不会立即执行，而是会将所有的操作按顺序存放在一个队列里，当你调用perform()方法时，队列中的事件会依次执行
    # perform立即执行动作链操作
    # move_by_offset中每一步的位置坐标都是针对上一步的位置的偏移量

    # action.move_by_offset(17, 0).perform()  # 此种方法会叠加之前的偏移量（因为是同一个动作链对象）
    ActionChains(webdri).move_by_offset(17, 0).perform()  # 不会叠加

    # # 下面打印，查看新坐标
    # new_drag = webdri.find_element_by_id('draggable')
    # print(new_drag.location)


# 释放动作链
action.release()