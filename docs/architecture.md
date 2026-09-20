# Architecture – Universe Android Netboot Level 3

## Core Principle
We do not fight the stock boot chain where it is strongest. We ride it, then replace the part that matters.

### High-Level Flow (Target)

1. Device powers on → stock PBL / XBL / ABL (or GBL path) runs as usual.
2. ABL is instructed (via specially crafted boot.img or other trigger) to load our payload instead of a normal Android kernel.
3. Our payload is a capable bootloader (primarily U-Boot, possibly with a custom thin stage in front).
4. Once control is in U-Boot (or equivalent):
   - Initialize USB gadget Ethernet (RNDIS/ECM) or other available network.
   - Perform DHCP / static config.
   - Fetch kernel + initramfs (and optionally rootfs via NBD) from a known host.
   - Boot the fetched image into a controlled environment (postmarketOS-style, custom recovery, agent runtime, etc.).

## Why This Path
- Replacing XBL/ABL entirely is extremely difficult on modern locked devices and risks permanent brick.
- Chainloading from ABL is proven on an increasing number of Qualcomm platforms via U-Boot work (Linaro, community, 2024–2026 progress).
- Once a real bootloader with network is running, classic PXE-like behavior becomes available.

## Network Priority Order
1. USB Ethernet gadget (most reliable early, works with host PC or OTG adapter)
2. Wired Ethernet if the device has it (rare on phones)
3. Wi-Fi (research only – drivers and firmware loading this early is the hardest problem)

## Host Side
A lightweight server (Python or Go preferred for portability) that can:
- Serve iPXE-like scripts or direct U-Boot scripts
- Provide TFTP for kernels
- Provide HTTP for larger payloads
- Provide NBD for full root filesystems
- Authenticate devices (MAC, certificate, or measured boot later)

## Safety Rules (Non-Negotiable)
- Every change must have a documented recovery path that does not require the netboot itself.
- Prefer temporary `fastboot boot` experiments before permanent flashing.
- Never flash unsigned or untested payloads to critical partitions without dual-slot or backup strategy.
- Document every device-specific quirk exhaustively.

## References We Build Upon
- Upstream U-Boot Qualcomm phone support
- Google Generic BootLoader (GBL) design
- postmarketOS network/live boot work
- Existing Android-PXE server apps (for inspiration on the reverse direction)

This document will evolve with every discovery.
