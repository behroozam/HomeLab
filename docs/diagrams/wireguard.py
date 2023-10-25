from urllib.request import urlretrieve , URLopener

from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.k8s.infra import Node, Master

vyos_icon = "vyos.png"

with Diagram("K3s Wireguard Network Design", show=False):
    with Cluster("K3s Cluster"):
        k3s = [
            Master("Wg: 172.16.74.3\n"
                + "LocalIP: 192.168.1.3"),
            Node("172.16.74.2\n"
                + "LocalIP: 192.168.1.2"),
            Node("172.16.74.1\n"
                + "LocalIP: 192.168.1.1")]

    vyos_cloud = Custom("VyOS Cloud Router\n" + "Wg: 172.16.74.4", vyos_icon)
    vyos_onprem = Custom("VyOS On-Prem Router\n" +
                          "Wg: 172.16.74.5\n" +
                          "LocalIP: 192.168.1.5", vyos_icon)

    vyos_onprem >> k3s >> vyos_onprem >> vyos_cloud >> vyos_onprem
