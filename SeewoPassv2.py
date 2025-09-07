import hashlib
import subprocess
import getpass
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import threading

def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

hugo = md5('hugo')

def enc(pwd):
    return md5(md5(pwd) + hugo)[8:24]

def trypwd(tar):
    for i in range(0, 1000000):
        pwd = f'{i:06}'
        if enc(pwd) == tar:
            return pwd
    return None

class SeewoPassGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("希沃管家密码解码工具")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        self.font = ("SimHei", 12)
        
        self.style = ttk.Style()
        if 'clam' in self.style.theme_names():
            self.style.theme_use('clam')
        
        self.style.configure(
            "Win11.TButton",
            font=self.font,
            padding=10,
            relief="flat",
            background="#0078d4",
            foreground="white",
            borderwidth=0,
            focuscolor="none"
        )
        
        try:
            self.style.configure(
                "Win11.TButton",
                borderradius=4
            )
        except:
            pass
        
        self.style.map(
            "Win11.TButton",
            background=[("active", "#106ebe")],
            relief=[("pressed", "sunken")]
        )
        
        self.create_main_window()
        self.current_choice = None
    
    def create_main_window(self):
        welcome_label = tk.Label(self.root, text="欢迎使用希沃管家密码解码工具！", font=("SimHei", 14, "bold"))
        welcome_label.pack(pady=15)
        
        version_label = tk.Label(self.root, text="当前使用的版本适用于希沃管家 【1.4.6】 版本", font=self.font)
        version_label.pack(pady=8)
        version_note_label = tk.Label(self.root, text="若您的电脑希沃管家版本高于此版本，请您先运行【3】！", font=self.font)
        version_note_label.pack(pady=8)
        
        choice_label = tk.Label(self.root, text="请选择要执行的操作：", font=self.font)
        choice_label.pack(pady=12)
        
        self.choice_var = tk.StringVar(value="1")
        
        radio_frame = tk.Frame(self.root)
        radio_frame.pack(pady=10, fill="x", padx=50)
        
        radio1 = tk.Radiobutton(
            radio_frame,
            text="【1】获取管理员密码",
            variable=self.choice_var,
            value="1",
            font=self.font,
            anchor="w",
            justify="left",
            height=2
        )
        radio1.pack(fill="x", pady=3)
        
        radio2 = tk.Radiobutton(
            radio_frame,
            text="【2】获取锁屏密码",
            variable=self.choice_var,
            value="2",
            font=self.font,
            anchor="w",
            justify="left",
            height=2
        )
        radio2.pack(fill="x", pady=3)
        
        radio3 = tk.Radiobutton(
            radio_frame,
            text="【3】拉起旧版希沃安装程序",
            variable=self.choice_var,
            value="3",
            font=self.font,
            anchor="w",
            justify="left",
            height=2
        )
        radio3.pack(fill="x", pady=3)
        
        radio4 = tk.Radiobutton(
            radio_frame,
            text="【4】拉起开源仓库页面",
            variable=self.choice_var,
            value="4",
            font=self.font,
            anchor="w",
            justify="left",
            height=2
        )
        radio4.pack(fill="x", pady=3)
        
        confirm_btn = ttk.Button(self.root, text="确定", style="Win11.TButton", width=25, command=self.on_confirm)
        confirm_btn.pack(pady=25)
    
    def on_confirm(self):
        self.current_choice = self.choice_var.get()
        
        if self.current_choice in ['1', '2']:
            self.handle_password_option()
        elif self.current_choice in ['3', '4']:
            self.handle_browser_option()
    
    def handle_password_option(self):
        current_user = getpass.getuser()
        
        if self.current_choice == '1':
            file_path = "C:\\ProgramData\\Seewo\\SeewoCore\\SeewoCore.ini"
            target_value = "PASSWORDV2"
            description = "管理员密码"
        else:
            file_path = f"C:\\Users\\{current_user}\\AppData\\Roaming\\Seewo\\SeewoAbility\\SeewoLockConfig.ini"
            target_value = "LockPasswardV2"
            description = "锁屏密码"
        
        try:
            subprocess.run(['notepad.exe', file_path], check=True, shell=True)
            messagebox.showinfo("提示", f"已自动打开配置文件：{file_path}\n请记录文件中的 {target_value} 值")
        except Exception as e:
            messagebox.showerror("错误", f"打开文件失败：{str(e)}")
            messagebox.showinfo("提示", f"请手动打开以下文件获取{description}值：\n{file_path}")
        
        tar = simpledialog.askstring("输入", f"请输入需要解密的 {target_value} 的值：")
        
        if tar:
            loading_window = tk.Toplevel(self.root)
            loading_window.title("处理中")
            loading_window.geometry("350x120")
            loading_window.resizable(False, False)
            
            loading_window.transient(self.root)
            loading_window.grab_set()
            
            loading_label = tk.Label(loading_window, text="请稍等片刻...", font=("SimHei", 12))
            loading_label.pack(pady=25)
            
            self.root.update_idletasks()
            x = self.root.winfo_x() + (self.root.winfo_width() - loading_window.winfo_width()) // 2
            y = self.root.winfo_y() + (self.root.winfo_height() - loading_window.winfo_height()) // 2
            loading_window.geometry(f"+{x}+{y}")
            
            def decode_password():
                ans = trypwd(tar)
                self.root.after(0, lambda: self.show_password_result(ans, loading_window, target_value))
            
            thread = threading.Thread(target=decode_password)
            thread.daemon = True
            thread.start()
    
    def show_password_result(self, ans, loading_window, target_value):
        loading_window.destroy()
        
        if ans is None:
            messagebox.showerror("错误", f"解码错误：检查您输入的值是否位于 {target_value} 字段！")
        else:
            messagebox.showinfo("密码结果", f"密码是：{ans}")
    
    def handle_browser_option(self):
        if self.current_choice == '3':
            url = "https://soft.wsyhn.com/soft/SeewoService_1.4.6.exe"
            message = "是否打开下载链接？"
            description = "下载程序"
        else:
            url = "https://github.com/yuyudifiesh/seewo-adminpassword-v2"
            message = "是否打开开源仓库页面？"
            description = "开源页面"
        
        if messagebox.askyesno("确认", message):
            try:
                webbrowser.open(url)
                messagebox.showinfo("提示", f"正在拉起{description}：{url}")
            except Exception as e:
                messagebox.showerror("错误", f"打开浏览器失败：{str(e)}")
                messagebox.showinfo("提示", f"如果浏览器没有自动打开，请手动复制上面的链接到浏览器中访问：\n{url}")

def main():
    root = tk.Tk()
    app = SeewoPassGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
