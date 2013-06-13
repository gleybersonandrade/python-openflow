"""Group Desc stats message."""
from pyof.v0x04.common.action import (
    ActionExperimenter, ActionSetField, ListOfActions)
from pyof.v0x04.common.flow_match import OxmClass, OxmOfbMatchField, OxmTLV
from pyof.v0x04.common.port import PortNo
from pyof.v0x04.controller2switch.common import Bucket, MultipartType
from pyof.v0x04.controller2switch.group_mod import GroupType, ListOfBuckets
from pyof.v0x04.controller2switch.multipart_reply import (
    GroupDescStats, MultipartReply)
from tests.test_struct import TestStruct


# class TestGroupStats(TestStruct):
#     """Group stats message."""

#     @classmethod
#     def setUpClass(cls):
#         """Configure raw file and its object in parent class (TestDump)."""
#         mp_type = MultipartType.OFPMP_GROUP_DESC
#         super().setUpClass()
#         super().set_raw_dump_file('v0x04', 'ofpt_group_desc_stats')
#         super().set_raw_dump_object(MultipartReply, xid=1,
#                                     multipart_type=mp_type,
#                                     flags=0,
#                                     body=_get_body())
#         super().set_minimum_size(16)


# def _get_body():
#     """Return the body used by MultipartReply message."""
#     oxmtlv1 = OxmTLV(oxm_class=OxmClass.OFPXMC_OPENFLOW_BASIC,
#                      oxm_field=OxmOfbMatchField.OFPXMT_OFB_METADATA,
#                      oxm_hasmask=False,
#                      oxm_value=b'\x00\x00\x00\x00\x00\x00\x00\x01')
#     action1 = ActionSetField(field=oxmtlv1)

#     oxmtlv2 = OxmTLV(oxm_class=OxmClass.OFPXMC_OPENFLOW_BASIC,
#                      oxm_field=OxmOfbMatchField.OFPXMT_OFB_METADATA,
#                      oxm_hasmask=False,
#                      oxm_value=b'\x00\x00\x00\x00\x00\x00\x00\x02')
#     action2 = ActionSetField(field=oxmtlv2)
#     action3 = ActionExperimenter(length=16, experimenter=0x00002320,
#                                  body=b'\x00\x0e\xff\xf8\x28\x00\x00\x00')

#     bucket1 = Bucket(length=48, weight=1, watch_port=PortNo.OFPP_ANY,
#                      watch_group=PortNo.OFPP_ANY,
#                      actions=ListOfActions([action1, action3]))
#     bucket2 = Bucket(length=48, weight=1, watch_port=PortNo.OFPP_ANY,
#                      watch_group=PortNo.OFPP_ANY,
#                      actions=ListOfActions([action2, action3]))

#     buckets = ListOfBuckets([bucket1, bucket2])
#     return GroupDescStats(length=104, group_type=GroupType.OFPGT_SELECT,
#                           group_id=1, buckets=buckets)
