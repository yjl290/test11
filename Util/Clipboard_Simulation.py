import win32clipboard as wc
import win32con
class Simulate_Clipboard:

    #读取剪切板
    @staticmethod
    def get_clipboard():
        #打开剪切板
        wc.OpenClipboard()
        #获取剪切板数据
        data = wc.GetClipboardData(win32con.CF_TEXT)
        #关闭剪切板
        wc.CloseClipboard()
        return data

    #设置剪切板内容
    @staticmethod
    def set_clipboard(content):
        wc.OpenClipboard()
        #清空剪切板
        wc.EmptyClipboard()
        #将数据astring写入剪切板
        wc.SetClipboardData(win32con.CF_UNICODETEXT, content)
        wc.CloseClipboard()