# from pyof.v0x04.symmetric.hello import (
#     Hello, HelloElemHeader, HelloElemType, ListOfHelloElements)
# import binascii

# def _new_list_of_elements():
#     """Crate new ListOfHelloElements."""
#     hello_elem = HelloElemHeader(HelloElemType.OFPHET_VERSIONBITMAP,
#                                  length=8, content=b'\x00\x00\x00\x10')
#     elements = ListOfHelloElements()
#     elements.append(hello_elem)
#     return elements

# hello = Hello(xid=62, elements=_new_list_of_elements())
# with open("/tmp/test.data", "bw") as fp: 
#     fp.write(hello.pack())
# print(binascii.a2b_hex(hello))

# from pyof.foundation.basic_types import FixedTypeList
# from pyof.v0x04.controller2switch.meter_mod import MeterMod, MeterBandHeader, MeterModCommand, MeterFlags, MeterBandType

# meter_header = MeterBandHeader(band_type=MeterBandType.OFPMBT_DROP, rate=0, burst_size=0)

# meter_mod = MeterMod(xid=1, command=MeterModCommand.OFPMC_ADD,
#                      flags=MeterFlags.OFPMF_KBPS, meter_id=1,
#                      bands=FixedTypeList(meter_header))

from pyof.v0x04.common.action import ActionOutput, ListOfActions
from pyof.foundation.basic_types import FixedTypeList
from pyof.v0x04.common.flow_instructions import (
    InstructionApplyAction, ListOfInstruction)
from pyof.v0x04.common.flow_match import (
    Match, MatchType, OxmClass, OxmOfbMatchField, OxmTLV)
from pyof.v0x04.common.port import PortNo
from pyof.v0x04.controller2switch.common import ListOfBucketCounter, MultipartType
from pyof.v0x04.controller2switch.multipart_reply import (
    BucketCounter, GroupStats, MultipartReply)

def _get_body():
    """Return the body used by MultipartReply message."""
    bs = ListOfBucketCounter([BucketCounter(packet_count=1, byte_count=1),
                        BucketCounter(packet_count=2, byte_count=2)])
    return GroupStats(length=72, group_id=1, ref_count=0,
                      packet_count=0, byte_count=0, duration_sec=14,
                      duration_nsec=837000000, bucket_stats=bs)

mr = MultipartReply(xid=1, multipart_type=MultipartType.OFPMP_GROUP, flags=0, body=_get_body())


with open("/tmp/mm.data", "bw") as fp: 
    fp.write(mr.pack())