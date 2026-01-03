import win32clipboard
import win32con

def get_clipboard_data(format_name, format_const):
    """Retrieve clipboard data for a given format constant."""
    try:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(format_const):
            data = win32clipboard.GetClipboardData(format_const)
            return data
        else:
            return None
    except Exception as e:
        return f"Error reading {format_name}: {e}"
    finally:
        win32clipboard.CloseClipboard()

if __name__ == "__main__":
    # Get plain text
    plain_text = get_clipboard_data("Plain Text", win32con.CF_UNICODETEXT)
    print("=== Plain Text ===")
    print(plain_text if plain_text else "[No plain text found]")

    # Get RTF (Rich Text Format)
    CF_RTF = win32clipboard.RegisterClipboardFormat("Rich Text Format")
    rtf_data = get_clipboard_data("RTF", CF_RTF)
    print("\n=== RTF Data ===")
    print(rtf_data if rtf_data else "[No RTF data found]")

    # Get HTML Format
    CF_HTML = win32clipboard.RegisterClipboardFormat("HTML Format")
    html_data = get_clipboard_data("HTML", CF_HTML)
    print("\n=== HTML Data ===")
    print(html_data if html_data else "[No HTML data found]")
