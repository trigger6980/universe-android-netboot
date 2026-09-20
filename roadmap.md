# Roadmap – Universe Android Netboot Level 3

## Phase 0 – Foundation (Current)
- [x] Repository created and vision locked
- [ ] Full architecture document
- [ ] Threat model & safety guidelines
- [ ] Survey of supported Qualcomm / other SoCs for U-Boot chainloading (2026 status)

## Phase 1 – Chainload Path (Most Practical Entry)
- Document and automate packaging U-Boot as an Android boot.img that ABL will accept
- Build minimal U-Boot configs for target devices with network + USB gadget support
- Host-side tools: simple TFTP/HTTP/NBD server tailored for phone netboot
- First successful live network boot on one supported device

## Phase 2 – Lightweight Early Stage
- Design a tiny pre-U-Boot or parallel stage that can initialize minimal network (USB Ethernet first)
- Explore whether GBL or custom EFI payload can be leveraged for earlier network
- Research Wi-Fi early-init possibilities (extremely hard, long-term)

## Phase 3 – Production Hardening
- Secure boot / measured boot considerations
- Remote attestation of the netbooted environment
- Integration with agent frameworks for automated phone fleets
- Diskless / read-only root + overlay patterns optimized for money-automation workloads

## Phase 4 – Fleet Scale
- Multi-device orchestration
- Zero-touch re-imaging
- Fallback and recovery paths that never brick

All work is committed to this repository. Nothing is kept private from Eric.
