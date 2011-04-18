#!/usr/bin/env python

import sys


map(
    sys.stdout.write,
    [
        ''.join(
            map(chr,
                (
                    [0x46,0x69,0x7A,0x7A,0x42,0x75,0x7A,0x7a] if not i % 0x0F else
                    [0x42,0x75,0x7A,0x7a] if not i % 0x05 else
                    [0x46,0x69,0x7A,0x7A] if not i % 0x03 else
                    [int(c) + 0x30 for c in str(i)]
                ) + [0x0A]
            )
        )
        for i in xrange(0x01, 0x65)
    ]
)


