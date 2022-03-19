from util import *
import json
import time
#username = sys.argv[1] # 登录账号
#password = sys.argv[2] # 登录密码
#img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def glados():
    try:
        driver = get_web_driver()
        driver.get("https://glados.rocks/console/checkin")
        with open(r'./glados_cookie.txt', 'r') as f:
            gla_cookie = json.load(f)
        driver.delete_all_cookies()
        for i in gla_cookie:
            driver.add_cookie(i)
        driver.get("https://glados.rocks/console/checkin")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[2]/button').click()
        print('glados check in success!')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    glados()
