import pyautogui
import time
import os

def move_mouse_to(x, y, duration=1):
    """Move the mouse to the specified coordinates."""
    try:
        pyautogui.moveTo(x, y, duration=duration)
        print(f"Moved mouse to ({x}, {y})")
    except Exception as e:
        print(f"Error moving mouse to ({x}, {y}): {e}")

def move_mouse_rel(x_offset, y_offset, duration=2):
    """Move the mouse relative to its current position."""
    try:
        pyautogui.moveRel(x_offset, y_offset, duration=duration)
        print(f"Moved mouse relative by ({x_offset}, {y_offset})")
    except Exception as e:
        print(f"Error moving mouse relative by ({x_offset}, {y_offset}): {e}")

def click_at(x, y, duration=1):
    """Click the mouse at the specified coordinates."""
    try:
        pyautogui.click(x, y, duration=duration)
        print(f"Clicked at ({x}, {y})")
    except Exception as e:
        print(f"Error clicking at ({x}, {y}): {e}")

def drag_mouse_rel(x_offset, y_offset, duration=1):
    """Drag the mouse relative to its current position."""
    try:
        pyautogui.dragRel(x_offset, y_offset, duration=duration)
        print(f"Dragged mouse relative by ({x_offset}, {y_offset})")
    except Exception as e:
        print(f"Error dragging mouse relative by ({x_offset}, {y_offset}): {e}")

def type_text(text):
    """Type the specified text."""
    try:
        pyautogui.typewrite(text)
        print(f"Typed text: {text}")
    except Exception as e:
        print(f"Error typing text: {e}")

def press_hotkey(*keys):
    """Press a combination of hotkeys."""
    try:
        pyautogui.hotkey(*keys)
        print(f"Pressed hotkeys: {' + '.join(keys)}")
    except Exception as e:
        print(f"Error pressing hotkeys: {e}")

def take_screenshot(directory, filename):
    """Take a screenshot and save it to the specified directory."""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        screenshot = pyautogui.screenshot()
        screenshot_path = os.path.join(directory, filename)
        screenshot.save(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
    except Exception as e:
        print(f"Error taking screenshot: {e}")

def main():
    """Main function to demonstrate various pyautogui functions and take screenshots."""
    try:
        move_mouse_to(100, 100, duration=1)
        move_mouse_rel(0, 50, duration=2)
        click_at(300, 300, duration=3)
        press_hotkey('ctrlleft', 'a')
        screenshot_directory = "screenshots"
        for i in range(5):
            take_screenshot(screenshot_directory, f"screenshot_{i + 1}.png")
            time.sleep(2)
    except Exception as e:
        print(f"Error in main function: {e}")

if __name__ == "__main__":
    main()

