"""只在本机终端配置密钥，不提供网页写入接口。"""
from getpass import getpass
from app import save_key


def main():
    key = getpass('百炼 API Key（输入不显示）：').strip()
    if not key.startswith('sk-') or any(c.isspace() for c in key):
        raise SystemExit('未保存：请输入有效的百炼模型 API Key。')
    save_key(key)
    print('已保存到当前用户的私有配置目录。请重启项目使配置生效。')


if __name__ == '__main__':
    main()
