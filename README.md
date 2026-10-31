# ios-sweet-camellia-build

Public, reproducible build of the XNU kernel used by the **camellia** (Xiaomi Redmi Note 10 5G,
MediaTek MT6833) iOS 16 port.

This repository contains only build glue and patches; it has no Apple firmware, no IPSW and no
device dumps.

## How it works

1. `blacktop/darwin-xnu-build` (pinned SHA) fetches Apple's open-source `xnu-8796` (macOS 13.5 /
   iOS 16 era).
2. The 0001-0081 bring-up patches come from the public `dipa-studio/ios-sweet` project (pinned SHA),
   fetched at build time.
3. `xnu/patches/0082-*..0116-*` in this repository add the camellia machine config, UFS/HFS root
   support, display console, `kminit`/`hw.target` fixes and the current diagnostics.
4. The kernel is built with `MACHINE_CONFIG=CAMELLIA`, `KERNEL_CONFIG=DEVELOPMENT`.

## Usage

Actions -> **xnu** -> **Run workflow** (`kernel_config = DEVELOPMENT`, `keep_going = true`).
The `xnu-kernel` artifact contains `kernel.development.camellia`.

## Credits

- Apple's `xnu-8796` source (APSL).
- `dipa-studio/ios-sweet` (SWEET bring-up patches).
- `blacktop/darwin-xnu-build` (build script).