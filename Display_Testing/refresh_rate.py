import pygetwindow as gw
import pyautogui
import time

def change_refresh_rate(window_title, width, height, refresh_rate):
    # Find the window by title
    window = gw.getWindowsWithTitle(window_title)

    if not window:
        print(f"Window with title '{window_title}' not found.")
        return

    # Activate the window
    window[0].activate()
    time.sleep(1)  # Wait for the window to be activated

    # Send key presses to navigate to the display settings (adjust as needed)
    pyautogui.hotkey('win', 'i')  # Opens Windows Settings
    time.sleep(1)
    pyautogui.write('system display settings')
    pyautogui.press('enter')
    time.sleep(1)

    # Send key presses to navigate within the display settings
    pyautogui.press('tab')  # Move to Display tab
    time.sleep(1)
    pyautogui.press(['down', 'down'])  # Move to Advanced display settings
    pyautogui.press('enter')
    time.sleep(1)

    # Send key presses to change the display settings
    pyautogui.press('tab')  # Move to Refresh rate
    pyautogui.press(['down'] * (refresh_rate - 60))  # Adjust as needed
    pyautogui.press('enter')
    time.sleep(1)

    # Close the settings window
    pyautogui.hotkey('alt', 'f4')

# Example usage
change_refresh_rate("Your Window Title", 1920, 1080, 144)
