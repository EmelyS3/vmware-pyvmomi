from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl


s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_1)
s.verify_mode=ssl.CERT_NONE
si= SmartConnect(host="192.168.1.211", user="root", pwd="Pxgtsjmnt201",sslContext=s)
content=si.content


def get_all_objs(content, vimtype):
        obj = {}

        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)

        for managed_object_ref in container.view:
                obj.update({managed_object_ref: managed_object_ref.name})
        return obj


getAllVms = get_all_objs(content, [vim.VirtualMachine])


for vm in getAllVms:
        print(vm.name)
