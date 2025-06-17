#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2025, NXP.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#

import binascii
import logging
import struct

from autopts.pybtp import defs
from autopts.pybtp.btp.btp import CONTROLLER_INDEX, get_iut_method as get_iut, \
    btp_hdr_check, pts_addr_get, pts_addr_type_get
from autopts.pybtp.types import BTPError, addr2btp_ba
from autopts.ptsprojects.stack import get_stack

log = logging.debug

HFP = {
    'read_supported_cmds': (defs.BTP_SERVICE_ID_HFP,
                            defs.BTP_HFP_CMD_READ_SUPPORTED_COMMANDS,
                            CONTROLLER_INDEX),
    'enable_slc': (defs.BTP_SERVICE_ID_HFP,
                   defs.BTP_HFP_CMD_ENABLE_SLC,
                   CONTROLLER_INDEX),
    'disable_slc': (defs.BTP_SERVICE_ID_HFP,
                    defs.BTP_HFP_CMD_DISABLE_SLC,
                    CONTROLLER_INDEX),
    'signal_strength_send': (defs.BTP_SERVICE_ID_HFP,
                             defs.BTP_HFP_CMD_SIGNAL_STRENGTH_SEND,
                             CONTROLLER_INDEX),
    'control': (defs.BTP_SERVICE_ID_HFP,
                defs.BTP_HFP_CMD_CONTROL,
                CONTROLLER_INDEX),
    'signal_strength_verify': (defs.BTP_SERVICE_ID_HFP,
                               defs.BTP_HFP_CMD_SIGNAL_STRENGTH_VERIFY,
                               CONTROLLER_INDEX),
    'ag_enable_call': (defs.BTP_SERVICE_ID_HFP,
                       defs.BTP_HFP_CMD_AG_ENABLE_CALL,
                       CONTROLLER_INDEX),
    'ag_discoverable': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_AG_DISCOVERABLE,
                        CONTROLLER_INDEX),
    'hf_discoverable': (defs.BTP_SERVICE_ID_HFP,
                        defs.BTP_HFP_CMD_HF_DISCOVERABLE,
                        CONTROLLER_INDEX),
    'enable_audio': (defs.BTP_SERVICE_ID_HFP,
                     defs.BTP_HFP_CMD_ENABLE_AUDIO,
                     CONTROLLER_INDEX),
    'disable_audio': (defs.BTP_SERVICE_ID_HFP,
                      defs.BTP_HFP_CMD_DISABLE_AUDIO,
                      CONTROLLER_INDEX),
}


def hfp_enable_slc(bd_addr=None, channel=None, is_ag=1, flags=0):
    logging.debug("%s %r %r %r", hfp_enable_slc.__name__, bd_addr, channel, is_ag)
    iutctl = get_iut()

    data_ba = bytearray()
    bd_addr_type_ba = struct.pack('B', pts_addr_type_get(defs.BTP_BR_ADDRESS_TYPE))
    bd_addr_ba = addr2btp_ba(pts_addr_get(bd_addr))

    data_ba.extend(bd_addr_type_ba)
    data_ba.extend(bd_addr_ba)
    data_ba.extend(struct.pack('B', channel))
    data_ba.extend(struct.pack('B', is_ag))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['enable_slc'], data=data_ba)


def hfp_disable_slc(flags=0):
    logging.debug("%s", hfp_disable_slc.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['disable_slc'], data=data_ba)


def hfp_signal_strength_send(strength, flags=0):
    logging.debug("%s %r", hfp_signal_strength_send.__name__, strength)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', strength))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['signal_strength_send'], data=data_ba)


def hfp_control(index, value, flags=0):
    logging.debug("%s %r %r", hfp_control.__name__, index, value)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', index))
    data_ba.extend(struct.pack('B', value))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['control'], data=data_ba)


def hfp_signal_strength_verify(strength, flags=0):
    logging.debug("%s %r", hfp_signal_strength_verify.__name__, strength)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', strength))
    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['signal_strength_verify'], data=data_ba)


def hfp_ag_enable_call(flags=0):
    logging.debug("%s", hfp_ag_enable_call.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_enable_call'], data=data_ba)


def hfp_ag_discoverable(flags=0):
    logging.debug("%s", hfp_ag_discoverable.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['ag_discoverable'], data=data_ba)


def hfp_hf_discoverable(flags=0):
    logging.debug("%s", hfp_hf_discoverable.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['hf_discoverable'], data=data_ba)


def hfp_enable_audio(flags=0):
    logging.debug("%s", hfp_enable_audio.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['enable_audio'], data=data_ba)


def hfp_disable_audio(flags=0):
    logging.debug("%s", hfp_disable_audio.__name__)
    iutctl = get_iut()

    data_ba = bytearray()

    data_ba.extend(struct.pack('B', flags))

    iutctl.btp_socket.send_wait_rsp(*HFP['disable_audio'], data=data_ba)


def hfp_command_rsp_succ(timeout=20.0):
    logging.debug("%s", hfp_command_rsp_succ.__name__)

    iutctl = get_iut()

    tuple_hdr, tuple_data = iutctl.btp_socket.read(timeout)
    logging.debug("received %r %r", tuple_hdr, tuple_data)

    btp_hdr_check(tuple_hdr, defs.BTP_SERVICE_ID_HFP)

    return tuple_data


# An example event, to be changed or deleted
def hfp_ev_dummy_completed(hfp, data, data_len):
    logging.debug('%s %r', hfp_ev_dummy_completed.__name__, data)

    fmt = '<B6sB'
    if len(data) < struct.calcsize(fmt):
        raise BTPError('Invalid data length')

    addr_type, addr, status = struct.unpack_from(fmt, data)

    addr = binascii.hexlify(addr[::-1]).lower().decode('utf-8')

    logging.debug(f'HFP Dummy event completed: addr {addr} addr_type '
                  f'{addr_type} status {status}')

    hfp.event_received(defs.BTP_HFP_EV_DUMMY_COMPLETED, (addr_type, addr, status))


def hfp_sco_connected_ev(hfp, data, data_len):
    logging.debug("%s %r %r", hfp_sco_connected_ev.__name__, data, data_len)

    stack = get_stack()
    stack.hfp.sco_connected = True
    hfp.event_received(defs.BTP_HFP_EV_SCO_CONNECTED, None)


def hfp_sco_disconnected_ev(hfp, data, data_len):
    logging.debug("%s %r %r", hfp_sco_disconnected_ev.__name__, data, data_len)

    stack = get_stack()
    stack.hfp.sco_connected = False
    hfp.event_received(defs.BTP_HFP_EV_SCO_DISCONNECTED, None)


HFP_EV = {
    defs.BTP_HFP_EV_DUMMY_COMPLETED: hfp_ev_dummy_completed,
    defs.BTP_HFP_EV_SCO_CONNECTED: hfp_sco_connected_ev,
    defs.BTP_HFP_EV_SCO_DISCONNECTED: hfp_sco_disconnected_ev,
}
