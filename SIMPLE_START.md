# Simplified Start – Universe Android Netboot

Eric, this is the cut-down path. No more dual-chamber theater. We build and move.

## Goal Right Now
Get a working temporary network boot path on a Pixel 3a (or equivalent) so the phone can load a clean environment from the host. Then put simple agents on it.

## Immediate Action Plan (Next 3 Steps)

### 1. Acquire Hardware
- Buy one used/refurbished Google Pixel 3a or 3a XL (target under $150).
- Prefer factory unlocked.
- Unlock bootloader the moment you have it (standard fastboot oem unlock).

### 2. Host Side (we start this now)
Create a minimal server that can serve:
- Kernel + initramfs via TFTP or HTTP
- Root filesystem via NBD or simple HTTP download + mount

### 3. First Test on Phone
- Use `fastboot boot` with a known-good postmarketOS or custom recovery image that has network support.
- Once it boots, pull a simple rootfs over USB Ethernet or Wi-Fi.
- Prove it works, document recovery, then iterate.

## What I Am Building in Parallel
- Simple Python host server skeleton
- Clear recovery checklist so we never brick
- Minimal agent placeholder that can run once the phone is netbooted

Everything goes into this repository. No hidden steps.
