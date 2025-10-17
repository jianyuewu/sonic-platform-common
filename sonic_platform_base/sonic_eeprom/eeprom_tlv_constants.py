# Copyright 2012 Cumulus Networks LLC, all rights reserved

#############################################################################
# TlvInfo EEPROM Constants
#
# This module contains only constant definitions with no dependencies.
# It can be imported quickly (few milliseconds) without loading heavy
# dependencies like redis or eeprom_base.
#
# These constants use the same naming convention as the TlvInfoDecoder class
# (with leading underscore) for direct compatibility.
#
# For code that needs TlvInfoDecoder class functionality, use:
#   from sonic_platform_base.sonic_eeprom.eeprom_tlvinfo import TlvInfoDecoder
#
# For code that only needs TLV constants (fast import), use:
#   from sonic_platform_base.sonic_eeprom.eeprom_tlv_constants import _TLV_CODE_*
#############################################################################

# Header Field Constants
_TLV_INFO_ID_STRING         = b"TlvInfo\x00"
_TLV_INFO_VERSION           = 0x01
_TLV_INFO_HDR_LEN           = 11
_TLV_INFO_MAX_LEN           = 2048
_TLV_TOTAL_LEN_MAX          = _TLV_INFO_MAX_LEN - _TLV_INFO_HDR_LEN
_TLV_HDR_ENABLED            = 1

# The Undefined TLV Type
_TLV_CODE_UNDEFINED         = 0xFC

# Default TLV Types
_TLV_CODE_PRODUCT_NAME      = 0x21
_TLV_CODE_PART_NUMBER       = 0x22
_TLV_CODE_SERIAL_NUMBER     = 0x23
_TLV_CODE_MAC_BASE          = 0x24
_TLV_CODE_MANUF_DATE        = 0x25
_TLV_CODE_DEVICE_VERSION    = 0x26
_TLV_CODE_LABEL_REVISION    = 0x27
_TLV_CODE_PLATFORM_NAME     = 0x28
_TLV_CODE_ONIE_VERSION      = 0x29
_TLV_CODE_MAC_SIZE          = 0x2A
_TLV_CODE_MANUF_NAME        = 0x2B
_TLV_CODE_MANUF_COUNTRY     = 0x2C
_TLV_CODE_VENDOR_NAME       = 0x2D
_TLV_CODE_DIAG_VERSION      = 0x2E
_TLV_CODE_SERVICE_TAG       = 0x2F
_TLV_CODE_VENDOR_EXT        = 0xFD
_TLV_CODE_CRC_32            = 0xFE

# By default disable the Quanta specific codes
_TLV_CODE_QUANTA_MAGIC      = _TLV_CODE_UNDEFINED
_TLV_CODE_QUANTA_CRC        = _TLV_CODE_UNDEFINED
_TLV_CODE_QUANTA_CARD_TYPE  = _TLV_CODE_UNDEFINED
_TLV_CODE_QUANTA_HW_VERSION = _TLV_CODE_UNDEFINED
_TLV_CODE_QUANTA_SW_VERSION = _TLV_CODE_UNDEFINED
_TLV_CODE_QUANTA_MANUF_DATE = _TLV_CODE_UNDEFINED
_TLV_CODE_QUANTA_MODEL_NAME = _TLV_CODE_UNDEFINED

# TLV Value Display Switch
_TLV_DISPLAY_VENDOR_EXT     = True
