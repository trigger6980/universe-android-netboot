# Recovery Rules – Never Brick

1. Always test with `fastboot boot <image>` first. Never flash until proven.
2. Keep a known-good stock boot.img and recovery.img for the Pixel 3a on the host.
3. If the phone fails to boot, hold Volume Down + Power to force fastboot mode.
4. From fastboot you can always `fastboot flash boot stock_boot.img` or `fastboot boot` a working image.
5. Document every command you run and the result in the GitHub repo.

The cable is your safety line. Network is a convenience, not a requirement for recovery.
