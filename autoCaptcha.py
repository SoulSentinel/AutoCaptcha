import os 
import time 
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://recruit.osiris.bar:50057/")

def get_image():
    img_element = driver.find_element(By.XPATH, "//img[@src]")
    img_src = img_element.get_attribute("src")

    # Extract the 'src' attributes from the <img> tags
    idx = img_src.find(',')
    img_src = img_src[idx+1::]
    return img_src

def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        # Encode the image as base64
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')


def main():
    directory = './captcha'  
    base64_dict = {}

    # hash local captcha images to base64
    for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            base64_str = image_to_base64(filepath)
            base64_dict[base64_str] = filename[:-4]

    for _ in range(12345):
        img_src = get_image()
        if img_src in base64_dict.keys(): 
            x = base64_dict[img_src]
            driver.find_element(By.NAME, "answer").send_keys(x)
            driver.find_element(By.TAG_NAME, "button").click()
        else: 
            print(False)


if __name__ == "__main__":
    main()

time.sleep(300)

# Close the driver when done
driver.close()