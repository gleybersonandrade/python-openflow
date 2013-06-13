from pyof.v0x04.common.action import (
    ActionExperimenter, ActionSetField, ListOfActions)
from pyof.v0x04.common.flow_match import OxmClass, OxmOfbMatchField, OxmTLV
from pyof.v0x04.common.port import PortNo
from pyof.v0x04.controller2switch.common import (
    Bucket, BucketCounter, ListOfBucketCounter, MultipartType)
from pyof.v0x04.controller2switch.group_mod import GroupType, ListOfBuckets
from pyof.v0x04.controller2switch.multipart_reply import (
    GroupDescStats, MultipartReply)

## NAO FUNCIONA ##

oxmtlv1 = OxmTLV(oxm_class=OxmClass.OFPXMC_OPENFLOW_BASIC,
                 oxm_field=OxmOfbMatchField.OFPXMT_OFB_METADATA,
                 oxm_hasmask=False,
                 oxm_value=b'\x00\x00\x00\x00\x00\x00\x00\x01')
oxmtlv2 = OxmTLV(oxm_class=OxmClass.OFPXMC_OPENFLOW_BASIC,
                 oxm_field=OxmOfbMatchField.OFPXMT_OFB_METADATA,
                 oxm_hasmask=False,
                 oxm_value=b'\x00\x00\x00\x00\x00\x00\x00\x02')

action1 = ActionSetField(field=oxmtlv1)
action2 = ActionSetField(field=oxmtlv2)
action3 = ActionExperimenter(length=16, experimenter=0x00002320,
                             body=b'\x00\x0e\xff\xf8\x28\x00\x00\x00')
action4 = ActionExperimenter(length=16, experimenter=0x00001223,
                             body=b'\x00\x0e\xff\xff\x28\x00\x00\x00')

bucket1 = Bucket(length=48, weight=1, watch_port=PortNo.OFPP_ANY,
                    watch_group=PortNo.OFPP_ANY,
                    actions=ListOfActions([action1, action2]))
bucket2 = Bucket(length=48, weight=1, watch_port=PortNo.OFPP_ANY,
                    watch_group=PortNo.OFPP_ANY,
                    actions=ListOfActions([action3, action4]))

buckets = ListOfBuckets([bucket1, bucket2])
buff = buckets.pack()
obj = ListOfBuckets()
obj.unpack(buff)




## FUNCIONA ##

# buckets = ListOfBucketCounter([BucketCounter(packet_count=0, byte_count=0),
#                                BucketCounter(packet_count=0, byte_count=0)])

# buff = buckets.pack()
# obj = ListOfBucketCounter()
# obj.unpack(buff)
