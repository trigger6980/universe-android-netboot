# Recommended Device for Level 3 – September 2026

## Primary Choice: Google Pixel 3a (or 3a XL)

**Target price**: Under $150 used / refurbished (well under the $300 limit).

### Why this phone
- Explicitly listed in postmarketOS **community** support tier (v26.06 and ongoing).
- Bootloader unlock is straightforward on factory-unlocked or non-Verizon models via standard fastboot.
- Strong existing documentation and community ports.
- Snapdragon 670 – sufficient performance for agent runtimes and netboot experiments.
- Low cost means low risk while we explore deep bootloader / early-network work.
- USB gadget support is mature in mainline ports, which is critical for the tethered NBD / Ethernet path we will use first.

### Secondary Options (also under $300)
- OnePlus 6 / 6T (Snapdragon 845 – better U-Boot proximity via SDM845 work)
- Xiaomi Poco F1 (Snapdragon 845, community support)
- Used Pixel 4a or 7a if you prefer newer hardware and still stay under $300 refurbished.

### Acquisition Notes
Prefer factory-unlocked units. Avoid pure carrier-locked devices when possible. Verify bootloader unlock status before purchase when buying used.

This device becomes the first hardware sandbox for the Universe Android Netboot project.
