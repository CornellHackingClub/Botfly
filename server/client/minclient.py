#!/usr/bin/env python
import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

