# Universe Netboot Host – Simplified

This is the first working piece.

## Quick Start
```bash
python3 simple_netboot_server.py --port 8080
```

Place boot files (kernel, initramfs, any rootfs tarball) into the `bootfiles/` directory that gets created.

## Next Real Steps
1. Unlock Pixel 3a bootloader.
2. Get a known-good recovery or postmarketOS initramfs that has USB gadget Ethernet.
3. Use `fastboot boot` to load it temporarily.
4. From the phone, pull files from this server over the USB network link.
5. Document every success and every recovery path in the main repo.

Keep it simple. Move forward.
