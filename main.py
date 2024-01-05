import sys

import frida
import psutil
import pathlib


def get_pid():
    process_name = "WeChatAppEx.exe"
    device = frida.get_local_device()
    processes = device.enumerate_processes()
    for process in processes:
        if process.name == process_name:
            cmdline = psutil.Process(process.pid).cmdline()
            # print(cmdline)
            if "--type=" not in cmdline:
                if not any('--type=' in arg for arg in cmdline):
                    print(process.pid)
                    return process.pid


def on_message(message, data):
    if message['type'] == 'send':
        print(message['payload'])
    elif message['type'] == 'error':
        print(message['stack'])


def load_address_source(version, bit):
    address_source = ""
    address_source_head_file_path = pathlib.Path(__file__).parent / f"Core/AddressSource.head"
    address_source_end_file_path = pathlib.Path(__file__).parent / f"Core/AddressSource.end"
    address_file_path = pathlib.Path(__file__).parent / f"Core/WeChatAppEx.exe/address_{version}_{bit}.json"
    hook_file_path = pathlib.Path(__file__).parent / f"Core/WeChatAppEx.exe/hook.js"

    try:
        assert address_file_path.exists(), f"File {address_file_path} does not exist"
        with open(address_source_head_file_path, 'r', encoding='utf-8') as f:
            address_source += f.read()
        with open(address_file_path, 'r', encoding='utf-8') as f:
            address_source += f.read()
        with open(address_source_end_file_path, 'r', encoding='utf-8') as f:
            address_source += f.read()
        with open(hook_file_path, 'r', encoding='utf-8') as f:
            address_source += f.read()
        print("HOOK文件组装成功!")
        return address_source
    except AssertionError as e:
        print(f"发生错误: {str(e)}")
        return None
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return None


if __name__ == '__main__':
    pid = get_pid()
    version = input("请输入版本号 (例如: 8531): ")
    session = frida.attach(pid)
    address = load_address_source(version,'x64')
    if address is not None:
        script = session.create_script(address)
        script.on('message', on_message)
        script.load()
        sys.stdin.read()
        session.detach()
