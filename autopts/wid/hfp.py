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

import logging
from autopts.pybtp.types import WIDParams
from autopts.pybtp import btp, defs
from autopts.wid import generic_wid_hdl
from autopts.ptsprojects.stack import get_stack
from time import sleep

log = logging.debug
ag_connected = False

def hfp_wid_hdl(wid, description, test_case_name):
    log(f'{hfp_wid_hdl.__name__}, {wid}, {description}, {test_case_name}')
    return generic_wid_hdl(wid, description, test_case_name, [__name__])


# wid handlers section begin
def hdl_wid_1(params: WIDParams):
    """
    Click Ok, then initiate a service level connection from the Implementation Under Test (IUT) to the PTS.
    """
    log("hdl_wid_1: Initiate a service level connection")

    # stack = get_stack()
    # stack.gap.set_passkey(None)
    #
    # if not stack.gap.is_connected():
    #     btp.gap_conn(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
    #     btp.gap_wait_for_connection()
    #
    # btp.gap_pair(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
    # sleep(3)

    if params.test_case_name in ['HFP/AG/SLC/BV-02-C']:
        return True
    if params.test_case_name in ['HFP/HF/SLC/BV-01-C']:
        return True
    if params.test_case_name in ['HFP/AG/SLC/BV-01-C']:
        return True
    if params.test_case_name in ['HFP/HF/SLC/BV-02-C']:
        return True
    if params.test_case_name in ['HFP/HF/SLC/BV-03-C']:
        return True
    if params.test_case_name in ['HFP/HF/SLC/BV-04-C']:
        return True
    if params.test_case_name in ['HFP/HF/SLC/BV-06-C']:
        return True
    if params.test_case_name in ['HFP/HF/ECS/BV-01-C']:
        return True
    if params.test_case_name in ['HFP/HF/ECS/BV-01-C']:
        return True
    if params.test_case_name.find('HFP/AG/') >= 0:
        if not ag_connected:
            btp.hfp_enable_slc(None, 1, 1)
    else:
        btp.hfp_enable_slc(None, 1, 0)
    return True


def hdl_wid_2(params: WIDParams):
    """
    Click Ok, then disable the service level connection using the Implementation Under Test (IUT).
    """
    log("hdl_wid_2: Disable service level connection")

    btp.hfp_disable_slc()
    global ag_connected
    ag_connected = False
    return True


def hdl_wid_12(params: WIDParams):
    """
    Click Ok, then place a call from an external line to the Implementation Under Test (IUT).
    Do not answer the call unless prompted to do so.
    """
    log("hdl_wid_12: External call to IUT")

    return True


def hdl_wid_91(params: WIDParams):
    """
    Delete the pairing with the PTS using the Implementation Under Test (IUT), then click Ok.
    """
    log("hdl_wid_91: Delete pairing with PTS")

    btp.gap_unpair()
    sleep(3)
    return True


def hdl_wid_220(params: WIDParams):
    """
    Is the IUT capable of establishing connection to an unpaired device?
    """
    log("hdl_wid_220: Confirming IUT can connect to unpaired device")

    btp.gap_set_conn()
    btp.gap_set_gendiscov()
    global ag_connected
    ag_connected = True
    return False


def hdl_wid_20000(params: WIDParams):
    """
    Please prepare IUT into a connectable mode in BR/EDR.
    Description: Verify that the Implementation Under Test (IUT) can accept GATT connect request from PTS.
    """
    log("hdl_wid_20000: Preparing IUT into connectable mode in BR/EDR")

    # Set device in discoverable and connectable mode
    btp.gap_set_conn()
    btp.gap_set_gendiscov()

    return True
