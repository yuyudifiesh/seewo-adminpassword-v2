import os
import hashlib
import subprocess
import getpass
import webbrowser

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

def main():
    current_user = getpass.getuser()
    print("欢迎使用希沃管家密码解码工具！")
    print("当前使用的版本适用于希沃管家 【1.4.6】 版本，若您的电脑希沃管家版本高于此版本，请您先运行【3】！")
    print("当前使用的版本适用于希沃管家 【1.4.6】 版本，若您的电脑希沃管家版本高于此版本，请您先运行【3】！")
    print("请选择要执行的操作：")
    print("【1】获取管理员密码（将打开 SeewoCore.ini ，请您记录 PASSWORDV2 的值）")
    print("【2】获取锁屏密码（将打开 SeewoLockConfig.ini ，请您记录 LockPasswardV2 的值）")
    print("【3】拉起安装程序（将为您下载希沃管家 1.4.6 版本安装包）")
    print("【4】拉起开源仓库页面（将为您打开 Github 开源仓库页面）")
    
    choice = input("请输入选项：")
    
    if choice == '1':
        file_path = "C:\\ProgramData\\Seewo\\SeewoCore\\SeewoCore.ini"
        target_value = "PASSWORDV2"
        description = "管理员密码"
        
        try:
            subprocess.run(['notepad.exe', file_path], check=True)
            print(f"已自动打开配置文件：{file_path}")
            print(f"请记录文件中的 {target_value} 值")
        except Exception as e:
            print(f"打开文件失败：{e}")
            print(f"请手动打开以下文件获取{description}值：")
            print(file_path)
        
        tar = input('请输入需要解密的 PASSWORDV2 的值：')
        print('请稍等片刻...')
        ans = trypwd(tar)
        if ans is None:
            print('解码错误：检查您输入的值是否位于 PASSWORDV2 字段！')
        else:
            print('密码是：' + ans)
        os.system('pause')
            
    elif choice == '2':
        file_path = f"C:\\Users\\{current_user}\\AppData\\Roaming\\Seewo\\SeewoAbility\\SeewoLockConfig.ini"
        target_value = "LockPasswardV2"
        description = "锁屏密码"
        
        try:
            subprocess.run(['notepad.exe', file_path], check=True)
            print(f"已自动打开配置文件：{file_path}")
            print(f"请记录文件中的 {target_value} 值")
        except Exception as e:
            print(f"打开文件失败：{e}")
            print(f"请手动打开以下文件获取{description}值：")
            print(file_path)
        
        tar = input('请输入需要解密的 LockPasswardV2 的值：')
        print('请稍等片刻...')
        ans = trypwd(tar)
        if ans is None:
            print('解码错误：检查您输入的值是否位于 LockPasswardV2 字段！')
        else:
            print('密码是：' + ans)
        os.system('pause')
            
    elif choice == '3':
        install_url = "https://soft.wsyhn.com/soft/SeewoService_1.4.6.exe"
        print(f"正在拉起下载程序：{install_url}")
        webbrowser.open(install_url)
        print("如果浏览器没有自动打开，请手动复制上面的链接到浏览器中访问")
        os.system('pause')

    elif choice == '4':
        open_url = "https://github.com/yuyudifiesh/seewo-adminpassword-v2"
        print(f"正在拉起开源页面：{open_url}")
        webbrowser.open(open_url)
        print("如果浏览器没有自动打开，请手动复制上面的链接到浏览器中访问")
        os.system('pause')
            
    else:
        print("无效的选项，程序将退出。")
        return

if __name__ == '__main__':
    main()
