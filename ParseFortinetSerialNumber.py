#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : ParseFortinetSerialNumber.py
# Author             : Podalirius (@podalirius_)
# Date created       : 10 Jan 2022

import argparse

# FortiGate ========================================
fortigate_sns = {
    # FortiGate 20
    "FGT20A": "FortiGate 20A",
    "FGT20B": "FortiGate 20B",
    "FGT20C": "FortiGate 20C",
    "FGT20D": "FortiGate 20D",
    "FGT20E": "FortiGate 20E",
    "FGT20F": "FortiGate 20F",
    # FortiGate 30
    "FGT30A": "FortiGate 30A",
    "FGT30B": "FortiGate 30B",
    "FGT30C": "FortiGate 30C",
    "FGT30D": "FortiGate 30D",
    "FGT30E": "FortiGate 30E",
    "FGT30F": "FortiGate 30F",
    # FortiGate 40
    "FGT40A": "FortiGate 40A",
    "FGT40B": "FortiGate 40B",
    "FGT40C": "FortiGate 40C",
    "FGT40D": "FortiGate 40D",
    "FGT40E": "FortiGate 40E",
    "FGT40F": "FortiGate 40F",
    # FortiGate 50
    "FGT50A": "FortiGate 50A",
    "FGT50B": "FortiGate 50B",
    "FGT50C": "FortiGate 50C",
    "FGT50D": "FortiGate 50D",
    "FGT50E": "FortiGate 50E",
    "FGT50F": "FortiGate 50F",
    # FortiGate 51
    "FGT51A": "FortiGate 51A",
    "FGT51B": "FortiGate 51B",
    "FGT51C": "FortiGate 51C",
    "FGT51D": "FortiGate 51D",
    "FGT51E": "FortiGate 51E",
    "FGT51F": "FortiGate 51F",
    # FortiGate 60
    "FGT60A": "FortiGate 60A",
    "FGT60B": "FortiGate 60B",
    "FGT60C": "FortiGate 60C",
    "FGT60D": "FortiGate 60D",
    "FGT60E": "FortiGate 60E",
    "FGT60F": "FortiGate 60F",
    # FortiGate 61
    "FGT61A": "FortiGate 61A",
    "FGT61B": "FortiGate 61B",
    "FGT61C": "FortiGate 61C",
    "FGT61D": "FortiGate 61D",
    "FGT61E": "FortiGate 61E",
    "FGT61F": "FortiGate 61F",
    # FortiGate 70
    "FGT70A": "FortiGate 70A",
    "FGT70B": "FortiGate 70B",
    "FGT70C": "FortiGate 70C",
    "FGT70D": "FortiGate 70D",
    "FGT70E": "FortiGate 70E",
    "FGT70F": "FortiGate 70F",
    # FortiGate 80
    "FGT80A": "FortiGate 80A",
    "FGT80B": "FortiGate 80B",
    "FGT80C": "FortiGate 80C",
    "FGT80D": "FortiGate 80D",
    "FGT80E": "FortiGate 80E",
    "FGT80F": "FortiGate 80F",
    # FortiGate 80CM
    "FG80CM": "FortiGate 80CM",
    # FortiGate 81
    "FGT81A": "FortiGate 81A",
    "FGT81B": "FortiGate 81B",
    "FGT81C": "FortiGate 81C",
    "FGT81D": "FortiGate 81D",
    "FGT81E": "FortiGate 81E",
    "FGT81F": "FortiGate 81F",
    # FortiGate 90
    "FGT90A": "FortiGate 90A",
    "FGT90B": "FortiGate 90B",
    "FGT90C": "FortiGate 90C",
    "FGT90D": "FortiGate 90D",
    "FGT90E": "FortiGate 90E",
    "FGT90F": "FortiGate 90F",
    # FortiGate 92
    "FGT92D": "FortiGate 92D",
    # FortiGate 100
    "FG100A": "FortiGate 100A",
    "FG100B": "FortiGate 100B",
    "FG100C": "FortiGate 100C",
    "FG100D": "FortiGate 100D",
    "FG100E": "FortiGate 100E",
    "FG100F": "FortiGate 100F",
    # FortiGate 101
    "FG101A": "FortiGate 101A",
    "FG101B": "FortiGate 101B",
    "FG101C": "FortiGate 101C",
    "FG101D": "FortiGate 101D",
    "FG101E": "FortiGate 101E",
    "FG101F": "FortiGate 101F",
    # FortiGate 111
    "FG10AH": "FortiGate 111A",
    "FG10BH": "FortiGate 111B",
    "FG10CH": "FortiGate 111C",
    "FG10DH": "FortiGate 111D",
    "FG10EH": "FortiGate 111E",
    "FG10FH": "FortiGate 111F",
    # FortiGate 140
    "FG140A": "FortiGate 140A",
    "FG140B": "FortiGate 140B",
    "FG140C": "FortiGate 140C",
    "FG140D": "FortiGate 140D",
    "FG140E": "FortiGate 140E",
    "FG140F": "FortiGate 140F",
    # FortiGate 200
    "FG200A": "FortiGate 200A",
    "FG200B": "FortiGate 200B",
    "FG200C": "FortiGate 200C",
    "FG200D": "FortiGate 200D",
    "FG200E": "FortiGate 200E",
    "FG200F": "FortiGate 200F",
    # FortiGate 201
    "FG201A": "FortiGate 201A",
    "FG201B": "FortiGate 201B",
    "FG201C": "FortiGate 201C",
    "FG201D": "FortiGate 201D",
    "FG201E": "FortiGate 201E",
    "FG201F": "FortiGate 201F",
    # FortiGate 240
    "FG240A": "FortiGate 240A",
    "FG240B": "FortiGate 240B",
    "FG240C": "FortiGate 240C",
    "FG240D": "FortiGate 240D",
    "FG240E": "FortiGate 240E",
    "FG240F": "FortiGate 240F",
    # FortiGate 280
    "FG280A": "FortiGate 280A",
    "FG280B": "FortiGate 280B",
    "FG280C": "FortiGate 280C",
    "FG280D": "FortiGate 280D",
    "FG280E": "FortiGate 280E",
    "FG280F": "FortiGate 280F",
    # FortiGate 300
    "FG300A": "FortiGate 300A",
    "FG300B": "FortiGate 300B",
    "FG300C": "FortiGate 300C",
    "FGT3HD": "FortiGate 300D",
    "FGT3HE": "FortiGate 300E",
    "FGT3HF": "FortiGate 300F",
    # FortiGate 310
    "FG310A": "FortiGate 310A",
    "FG310B": "FortiGate 310B",
    "FG310C": "FortiGate 310C",
    "FG310D": "FortiGate 310D",
    "FG310E": "FortiGate 310E",
    "FG310F": "FortiGate 310F",
    # FortiGate 311
    "FG311A": "FortiGate 311A",
    "FG311B": "FortiGate 311B",
    "FG311C": "FortiGate 311C",
    "FG311D": "FortiGate 311D",
    "FG311E": "FortiGate 311E",
    "FG311F": "FortiGate 311F",
    # FortiGate 400
    "FG400A": "FortiGate 400A",
    "FG400B": "FortiGate 400B",
    "FG400C": "FortiGate 400C",
    "FGT4HD": "FortiGate 400D",
    "FGT4HE": "FortiGate 400E",
    "FGT4HF": "FortiGate 400F",
    # FortiGate 500
    "FG500A": "FortiGate 500A",
    "FG500B": "FortiGate 500B",
    "FG500C": "FortiGate 500C",
    "FGT5HD": "FortiGate 500D",
    "FGT5HE": "FortiGate 500E",
    "FGT5HF": "FortiGate 500F",
    # FortiGate 501
    "FG501E": "FortiGate 501E",
    # FortiGate 600
    "FG600A": "FortiGate 600A",
    "FG600B": "FortiGate 600B",
    "FG600C": "FortiGate 600C",
    "FGT6HD": "FortiGate 600D",
    "FGT6HE": "FortiGate 600E",
    "FGT6HF": "FortiGate 600F",
    # FortiGate 800
    "FGT800": "FortiGate 800",
    "FG800A": "FortiGate 800A",
    "FG800B": "FortiGate 800B",
    "FG800C": "FortiGate 800C",
    "FG800D": "FortiGate 800D",
    "FG800E": "FortiGate 800E",
    "FG800F": "FortiGate 800F",
    # FortiGate 900
    "FG900A": "FortiGate 900A",
    "FG900B": "FortiGate 900B",
    "FG900C": "FortiGate 900C",
    "FG900D": "FortiGate 900D",
    "FG900E": "FortiGate 900E",
    "FG900F": "FortiGate 900F",
    # FortiGate 1000
    "FGT1KA": "FortiGate 1000A",
    "FGT1KB": "FortiGate 1000B",
    "FGT1KC": "FortiGate 1000C",
    "FGT1KD": "FortiGate 1000D",
    "FGT1KE": "FortiGate 1000E",
    "FGT1KF": "FortiGate 1000F",
    "FGT1KX": "FortiGate 1000X",  # ?
    # FortiGate 1200
    "FG1K2A": "FortiGate 1000A",
    "FG1K2B": "FortiGate 1000B",
    "FG1K2C": "FortiGate 1000C",
    "FG1K2D": "FortiGate 1000D",
    "FG1K2E": "FortiGate 1000E",
    "FG1K2F": "FortiGate 1000F",
    # FortiGate 1500
    "FG1K5A": "FortiGate 1500A",
    "FG1K5B": "FortiGate 1500B",
    "FG1K5C": "FortiGate 1500C",
    "FG1K5D": "FortiGate 1500D",
    "FG1K5E": "FortiGate 1500E",
    "FG1K5F": "FortiGate 1500F",
    # FortiGate 3000
    "FG3K0A": "FortiGate 3000A",
    "FG3K0B": "FortiGate 3000B",
    "FG3K0C": "FortiGate 3000C",
    "FG3K0D": "FortiGate 3000D",
    "FG3K0E": "FortiGate 3000E",
    "FG3K0F": "FortiGate 3000F",
    # FortiGate 3016
    "FGT3KB": "FortiGate 3016B",
    # FortiGate 3100
    "FG3K1A": "FortiGate 3100A",
    "FG3K1B": "FortiGate 3100B",
    "FG3K1C": "FortiGate 3100C",
    "FG3K1D": "FortiGate 3100D",
    "FG3K1E": "FortiGate 3100E",
    "FG3K1F": "FortiGate 3100F",
    # FortiGate 3200
    "FG3K2A": "FortiGate 3200A",
    "FG3K2B": "FortiGate 3200B",
    "FG3K2C": "FortiGate 3200C",
    "FG3K2D": "FortiGate 3200D",
    "FG3K2E": "FortiGate 3200E",
    "FG3K2F": "FortiGate 3200F",
    # FortiGate 3600
    "FG3K6A": "FortiGate 3600A",
    "FG3K6B": "FortiGate 3600B",
    "FG3K6C": "FortiGate 3600C",
    "FG3K6D": "FortiGate 3600D",
    "FG3K6E": "FortiGate 3600E",
    "FG3K6F": "FortiGate 3600F",
    # FortiGate 3800
    "FG3K8A": "FortiGate 3800A",
    "FG3K8B": "FortiGate 3800B",
    "FG3K8C": "FortiGate 3800C",
    "FG3K8D": "FortiGate 3800D",
    "FG3K8E": "FortiGate 3800E",
    "FG3K8F": "FortiGate 3800F",
    # FortiGate 3900
    "FG3K9A": "FortiGate 3900A",
    "FG3K9B": "FortiGate 3900B",
    "FG3K9C": "FortiGate 3900C",
    "FG3K9D": "FortiGate 3900D",
    "FG3K9E": "FortiGate 3900E",
    "FG3K9F": "FortiGate 3900F",
    # FortiGate 3901
    "FG3K91": "FortiGate 3901",
    # FortiGate 5001
    "FG-5KB": "FortiGate 5001B",
    "FG-5KC": "FortiGate 5001C",
    "FG5AD1": "FortiGate 5001A-DW",
    # FortiGate Virtual Machines =======================
    "FGVM00": "FortiGate VM ",
    "FGVM02": "FortiGate VM ",
    "FGVM2V": "FortiGate VM "
}

# FortiWifi ======================================
fortiwifi_sns = {
    # FortiWifi 20
    "FWF20A": "FortiWifi 20A",
    "FWF20B": "FortiWifi 20B",
    "FWF20C": "FortiWifi 20C",
    "FWF20D": "FortiWifi 20D",
    "FWF20E": "FortiWifi 20E",
    "FWF20F": "FortiWifi 20F",
    # FortiWifi 30
    "FWF30A": "FortiWifi 30A",
    "FWF30B": "FortiWifi 30B",
    "FWF30C": "FortiWifi 30C",
    "FWF30D": "FortiWifi 30D",
    "FWF30E": "FortiWifi 30E",
    "FWF30F": "FortiWifi 30F",
    # FortiWifi 40
    "FWF40A": "FortiWifi 40A",
    "FWF40B": "FortiWifi 40B",
    "FWF40C": "FortiWifi 40C",
    "FWF40D": "FortiWifi 40D",
    "FWF40E": "FortiWifi 40E",
    "FWF40F": "FortiWifi 40F",
    # FortiWifi 50
    "FWF50A": "FortiWifi 50A",
    "FWF50B": "FortiWifi 50B",
    "FWF50C": "FortiWifi 50C",
    "FWF50D": "FortiWifi 50D",
    "FWF50E": "FortiWifi 50E",
    "FWF50F": "FortiWifi 50F",
    # FortiWifi 60
    "FWF60A": "FortiWifi 60A",  # https://community.fortinet.com/t5/Fortinet-Forum/Reset-admin-password-of-a-FortiWifi-60A/m-p/13860
    "FWF60B": "FortiWifi 60B",
    "FWF60C": "FortiWifi 60C",
    "FWF60D": "FortiWifi 60D",
    "FWF60E": "FortiWifi 60E",
    "FWF60F": "FortiWifi 60F",
    # FortiWifi 60CM
    "FW60CM": "FortiWifi 60CM",
    # FortiWifi 60DC
    "FW60DC": "FortiWifi 60DC",
    # FortiWifi 61
    "FWF61A": "FortiWifi 61A",
    "FWF61B": "FortiWifi 61B",
    "FWF61C": "FortiWifi 61C",
    "FWF61D": "FortiWifi 61D",
    "FWF61E": "FortiWifi 61E",
    "FWF61F": "FortiWifi 61F",
    # FortiWifi 80
    "FWF80F": "FortiWifi 80F",
    # FortiWifi 80CM
    "FW80CM": "FortiWifi 80CM",
    # FortiWifi 81
    "FWF81F": "FortiWifi 81F",
    # FortiWifi 90
    "FWF90D": "FortiWifi 90D",
    # FortiWifi 92
    "FWF92D": "FortiWifi 92D",
}

# FortiMail ======================================
fortimail_sns = {
    # FortiMail 100
    "FE-100": "FortiMail 100",
    "FE100C": "FortiMail 100C",
    # FortiMail 200
    "FE200D": "FortiMail 200D",
    # FortiMail 400
    "FE-400": "FortiMail 400",
    "FE400B": "FortiMail 400B",
    # FortiMail 3000
    "FE-3KD": "FortiMail 3000D",
}

# FortiManager ===================================
fortimanager_sns = {
    # FortiManager 100
    "FMG100": "FortiManager 100",
    # FortiManager 400
    "FM400B": "FortiManager 400B",
}

# FortiAnalyzer ==================================
fortianalyzer_sns = {
    # FortiAnalyzer 100
    "FL100B": "FortiAnalyzer 100B",
    # FortiAnalyzer 200
    "FL200D": "FortiAnalyzer 200D",
    # FortiAnalyzer 800
    "FL800B": "FortiAnalyzer 800B",
}

# FortiAP ========================================
fortiap_sns = {
    # FortiAP 220
    "FAP22B": "FortiAP 220B",
    # FortiAP 220
    "FP221B": "FortiAP 221B",
}

# FortiAuthenticator =============================
fortiauthenticator_sns = {
    # FortiAuthenticator 200
    "FAC2HD": "FortiAuthenticator 200D",
}


def dictmerge(*srcdicts):
    out = {}
    # On itere sur les dicts passés en param
    for sd in srcdicts:
        # On itere sur lesclés de chaque dict
        for key in sd.keys():
            # Si on ne la connait pas déjà, on crée la clé dans le dict de sortie
            if key not in out.keys():
                out[key] = sd[key]
            # Sinon, on vérifie la condition avant de l'ajouter (on l'ajoute que si elle est plus petite)
            else:
                if sd[key] < out[key]:
                    out[key] = sd[key]
    return out


def parse_forti_sn(sn, data, verbose=False):
    sn = sn.upper().strip()
    if len(sn) == 16:
        ftype, number = sn[:6], sn[6:]
        if ftype in data:
            return {"fullname": data[ftype], "number": number, "model": ftype, "sn": sn}
        else:
            if verbose:
                print("[!] Unknown model %s (%s)" % (ftype, sn))
            return None
    else:
        if verbose:
            print("[!] Invalid SN length: %d (%s)" % (len(sn), sn))
        return None


def parseArgs():
    parser = argparse.ArgumentParser(description="Description message")
    parser.add_argument("serial", default=None, help='Fortinet serial number.')
    parser.add_argument("-v", "--verbose", default=False, action='store_true', help='Verbose mode. (default: False)')
    return parser.parse_args()


if __name__ == '__main__':
    options = parseArgs()

    fortinet_serial_number_patterns = dictmerge([fortigate_sns, fortiwifi_sns, fortimail_sns, fortimanager_sns, fortianalyzer_sns, fortiap_sns, fortiauthenticator_sns])

    if options.verbose:
        print("[>] Loaded %d serial number patterns." % len(fortinet_serial_number_patterns.keys()))

    result = parse_forti_sn(options.serial, fortinet_serial_number_patterns, verbose=True)

    if result is not None:
        print("[+] Detected %s (%s-%s)" % (result["fullname"], result["model"], result["number"]))
    else:
        print("[!] Could not detect model from serial number.")
