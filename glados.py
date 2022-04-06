from util import *
import json
import time

#username = sys.argv[1] # 登录账号
#password = sys.argv[2] # 登录密码
#img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=3)
def glados():
    try:
        driver = get_web_driver()
        driver.get("https://glados.rocks/console/checkin")
        print(sys.argv[1])
        gla_cookie = json.loads(sys.argv[1])
        print(gla_cookie)
        driver.delete_all_cookies()
        for i in gla_cookie:
            driver.add_cookie(i)
        driver.get("https://glados.rocks/console/checkin")
        time.sleep(3)
        driver.find_elements_by_class_name('button')[0].click()
        print('glados check in success!')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    glados()
