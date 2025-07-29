import os
import re
import win32com.client


select_num = int(input(">"))

def main():
    
    pass


"""
deviceなどIDをprint
detected_miscリストに追加
"""
def get_device_info():    
    wmi_service = win32com.client.GetObject("winmgmts:")
    mouse_devices = wmi_service.InstancesOf("Win32_PointingDevice")# 全てのデバイスを取得
    detected_mice = []# 検出されたデバイスlist

    for device in mouse_devices:
        device_name = device.Name # デバイス名を取得
        id_match = re.search(r'VID_(\w+)&PID_(\w+)', device.PNPDeviceID) # PNPDeviceIDからVIDとPIDを抽出
        vid, pid = id_match.groups() if id_match else (None, None) # デバイス名、VID、PIDをリストに追加
        # 出力
        print(f"Device_Name:{device_name}")
        print(f"PNPDeviceID:{device.PNPDeviceID}")
        print(f"vid:{vid}",f"pid:{pid}")
        print("_______________________")
    
        detected_mice.append((device_name, vid, pid))