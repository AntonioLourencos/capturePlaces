from time import sleep

FEED = "window.document.querySelector('[role=feed]')"


def scrollDown(driver):
    last_height = driver.execute_script(f"return {FEED}.scrollHeight")

    while True:
        driver.execute_script(f"{FEED}.scrollTo(0, {FEED}.scrollHeight);")

        sleep(3)

        height = driver.execute_script(f"return {FEED}.scrollHeight")

        if height == last_height:
            break

        last_height = height
