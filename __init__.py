import ctypes
import win32gui
import win32process

def get_keyboard_language():
    """
    Get the current input language of the active window.
    Returns:
        str: Hex code of the current language (e.g., '0x409').
    """
    hwnd = win32gui.GetForegroundWindow()
    thread_id = win32process.GetWindowThreadProcessId(hwnd)[0]
    layout_id = ctypes.windll.user32.GetKeyboardLayout(thread_id)
    language_id = layout_id & 0xFFFF  # Extract low word
    return hex(language_id)

def get_language_name(lang_hex):
    """
    Convert language hex code to human-readable name.
    
    Args:
        lang_hex (str): Language hex code (e.g., '0x409')
        
    Returns:
        str: Language name
    """
    languages = {
        '0x409': 'English (US)',
        '0x801': 'Arabic (Saudi Arabia)',
        '0xc01': 'Arabic (Egypt)',
        '0x1401': 'Arabic (Algeria)',
        '0x3c01': 'Arabic (UAE)',
    }
    return languages.get(lang_hex, f'Unknown Language: {lang_hex}')

if __name__ == "__main__":
    lang_hex = get_keyboard_language()
    lang_name = get_language_name(lang_hex)
    print(f"Lang : {lang_name}")
