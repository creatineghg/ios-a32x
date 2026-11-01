#!/usr/bin/env python3
"""Make dxb/build.sh fail the build when a local SWEET patch does not apply.

Upstream ios-sweet patches (0001-0081) may legitimately be already applied.
Our local patches (0082+) must apply cleanly; a skipped local patch silently
changes the kernel under test, which has burned whole evenings.
"""
import pathlib
import sys

BUILD = pathlib.Path("dxb/build.sh")
OLD = ('                warning "Skipping patch ${PATCH} '
       '(already upstream, previously applied, or malformed): ${APPLY_CHECK}"')
NEW = '''                case "${PATCH##*/}" in
                  008[2-9]*|009[0-9]*|01[0-9][0-9]*) error "Local patch did not apply: ${PATCH} (${APPLY_CHECK})"; exit 1 ;;
                  *) warning "Skipping patch ${PATCH} (already upstream, previously applied, or malformed): ${APPLY_CHECK}" ;;
                esac'''

def main() -> int:
    text = BUILD.read_text()
    if OLD not in text:
        print("harden_patches: skip block not found; refusing to build unverified", file=sys.stderr)
        return 1
    BUILD.write_text(text.replace(OLD, NEW))
    print("harden_patches: local patches (0082+) now fail the build when they do not apply")
    return 0

if __name__ == "__main__":
    sys.exit(main())
