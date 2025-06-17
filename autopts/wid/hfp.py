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
from autopts.pybtp.types import WIDParams, IOCap
from autopts.pybtp import btp, defs
from autopts.wid import generic_wid_hdl
from autopts.ptsprojects.stack import get_stack
from time import sleep

log = logging.debug


def hfp_wid_hdl(wid, description, test_case_name):
    log(f'{hfp_wid_hdl.__name__}, {wid}, {description}, {test_case_name}')
    return generic_wid_hdl(wid, description, test_case_name, [__name__])


# wid handlers section begin
def hdl_wid_1(params: WIDParams):
    """
    Click Ok, then initiate a service level connection from the Implementation Under Test (IUT) to the PTS.
    """
    log("hdl_wid_1: Initiate a service level connection")

    stack = get_stack()
    stack.gap.set_passkey(None)

    if not stack.gap.is_connected():
        btp.gap_conn(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
        btp.gap_wait_for_connection()

    btp.gap_pair(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)

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
        if not stack.hfp.is_sco_connected():
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
    return True


def hdl_wid_3(params: WIDParams):
    """
        Click Ok, then initiate an audio connection (SCO) from the Implementation Under Test (IUT) to the PTS.
    """
    sleep(3)
    if params.test_case_name in ['HFP/HF/ATA/BV-02-C'] or params.test_case_name in [
        'HFP/HF/ATH/BV-03-C'] or params.test_case_name in ['HFP/HF/ATH/BV-04-C'] or params.test_case_name in [
        'HFP/HF/ATH/BV-09-C']:
        return True
    btp.hfp_enable_audio()
    return True


def hdl_wid_4(params: WIDParams):
    """
        Click Ok, then close the audio connection (SCO)
        between the Implementation Under Test (IUT) and the PTS. Do
        not close the serivice level connection (SLC) or power-off the IUT..
    """
    btp.hfp_disable_audio()
    return True


def hdl_wid_12(params: WIDParams):
    """
    Click Ok, then place a call from an external line to the Implementation Under Test (IUT).
    Do not answer the call unless prompted to do so.
    """
    if params.test_case_name in ['HFP/AG/ACC/BV-09-C']:
        sleep(3)
    log("hdl_wid_12: External call to IUT")
    btp.hfp_ag_enable_call()
    return True


def hdl_wid_35(params: WIDParams):
    """
    Verify the presence of an audio connection, then click Ok.
    """
    log("hdl_wid_35: Verify presence of audio connection")

    if params.test_case_name in ['HFP/HF/ICA/BV-01-C']:
        sleep(1)
    stack = get_stack()
    if stack.hfp.is_sco_connected():
        return True
    else:
        stack.hfp.wait_sco_connected_ev(2)
        if not stack.hfp.is_sco_connected():
            # if keep waiting here, it blocks the doggle to reply the SCO HCI_Connection_Request HCI cmd.
            if params.test_case_name in ['HFP/AG/ACS/BV-10-C'] or params.test_case_name in [
                'HFP/AG/ACC/BV-23-C'] or params.test_case_name in ['HFP/AG/ACC/BV-25-C']:
                stack.hfp.need_check_sco_connection = True
                return True
            elif params.test_case_name in ['HFP/AG/OOR/BV-01-C'] or params.test_case_name in ['HFP/AG/ATH/BV-03-C']:
                stack.hfp.need_check_sco_connection = True
                return True
            elif params.test_case_name in ['HFP/AG/TCA/BV-01-C'] or params.test_case_name in ['HFP/AG/ATH/BV-03-C']:
                stack.hfp.need_check_sco_connection = True
                return True
            elif params.test_case_name in ['HFP/HF/TDC/BV-01-C']:
                stack.hfp.need_check_sco_connection = True
                return True
            elif params.test_case_name in ['HFP/HF/ATH/BV-06-C']:
                stack.hfp.need_check_sco_connection = True
                return True
            elif params.test_case_name in ['HFP/HF/RSV/BV-03-C']:
                stack.hfp.need_check_sco_connection = True
                return True
            elif params.test_case_name in ['HFP/HF/ECC/BV-01-C']:
                stack.hfp.need_check_sco_connection = True
                return True
            elif params.test_case_name in ['HFP/AG/ICA/BV-02-C']:
                stack.hfp.need_check_sco_connection = True
                return True
            else:
                return False
        return True


def hdl_wid_53(params: WIDParams):
    """
    Verify that the signal reported on the Implementation Under Test (IUT) is proportional to the value (out of 5), then click Ok.
    """
    log(f"hdl_wid_53: Verify signal strength indication on IUT: {params.description[-1]}")

    sleep(7)
    if params.description[-1] == '5':
        if params.test_case_name in ['HFP/AG/PSI/BV-01-C']:
            btp.hfp_signal_strength_send(5)
        btp.hfp_signal_strength_verify(5)
    elif params.description[-1] == '4':
        if params.test_case_name in ['HFP/AG/PSI/BV-01-C']:
            btp.hfp_signal_strength_send(4)
        btp.hfp_signal_strength_verify(4)
    elif params.description[-1] == '3':
        if params.test_case_name in ['HFP/AG/PSI/BV-01-C']:
            btp.hfp_signal_strength_send(3)
        btp.hfp_signal_strength_verify(3)
    elif params.description[-1] == '2':
        if params.test_case_name in ['HFP/AG/PSI/BV-01-C']:
            btp.hfp_signal_strength_send(2)
        btp.hfp_signal_strength_verify(2)
    elif params.description[-1] == '1':
        btp.hfp_signal_strength_verify(1)

    return True


def hdl_wid_91(_: WIDParams):
    """
    Delete the pairing with the PTS using the Implementation Under Test (IUT), then click Ok.
    """
    log("hdl_wid_91: Delete pairing with PTS")

    btp.gap_unpair()
    sleep(3)
    return True


def hdl_wid_94(_: WIDParams):
    """
    Click Ok, then move the PTS and the Implementation Under Test (IUT) out of range of each other.
    """
    log("hdl_wid_94: Move IUT out of range")

    # For automated testing, we can simulate going out of range by:
    # 1. Disconnecting the connection
    # 2. Or setting a flag to simulate out of range condition

    # Disconnect to simulate out of range
    sleep(1)
    btp.hfp_disable_slc()
    btp.gap_disconn(bd_addr_type=defs.BTP_BR_ADDRESS_TYPE)
    sleep(2)

    return True


def hdl_wid_95(params: WIDParams):
    """
    Click Ok, then remove the Implementation Under Test (IUT) and/or the PTS from the RF shield.
    If the out of range method was used, bring the IUT and PTS back within range.
    """
    log("hdl_wid_95: Bring IUT back within range")

    # Simulate bringing devices back within range by re-establishing connection
    sleep(1)

    btp.gap_set_conn()
    btp.gap_set_gendiscov()
    if params.test_case_name.find('HFP/AG/') >= 0:
        btp.hfp_ag_discoverable()
    elif params.test_case_name.find('HFP/HF/') >= 0:
        btp.hfp_ag_discoverable()
    btp.gap_set_io_cap(IOCap.no_input_output)

    return True


def hdl_wid_175(params: WIDParams):
    """
    Click OK. Then, impair the signal to the AG so that a reduction in signal strength can be observed.
    """
    log("hdl_wid_175: Impair signal to AG for signal strength reduction")
    btp.hfp_control(defs.HFP_IMPAIR_SIGNAL, 1)
    return True


def hdl_wid_220(params: WIDParams):
    """
    Is the IUT capable of establishing connection to an unpaired device?
    """
    log("hdl_wid_220: Confirming IUT can connect to unpaired device")

    btp.gap_set_conn()
    btp.gap_set_gendiscov()
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
