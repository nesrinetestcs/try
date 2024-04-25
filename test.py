import platform

def is_running_on_vm():
    # Check if the system platform is a common VM platform
    vm_platforms = ['VMware', 'VirtualBox', 'QEMU', 'KVM', 'Hyper-V', 'Xen', 'Parallels']
    if any(platform in platform.platform() for platform in vm_platforms):
        return True
    else:
        return False

if __name__ == "__main__":
    if is_running_on_vm():
        print("This script cannot be executed on a virtual machine.")
    else:
        print("Script execution allowed.")
        # Add your script's main functionality here
