#!/usr/bin/env python
import os
config = {
    "default_actions": [
        'clobber',
        'checkout-gecko',
        'download-gonk',
        'unpack-gonk',
        'checkout-gaia',
        'checkout-gaia-l10n',
        'build',
        'build-symbols',
        'make-updates',
        'prep-upload',
        'upload',
    ],
    "ssh_key": os.path.expanduser("~/.ssh/b2gbld_dsa"),
    "ssh_user": "b2gbld",
    "upload_remote_host": "pvtbuilds2.dmz.scl3.mozilla.com",
    "upload_remote_basepath": "/pub/mozilla.org/b2g/tinderbox-builds",
    "upload_remote_nightly_basepath": "/pub/mozilla.org/b2g/nightly",
    "tooltool_servers": ["http://runtime-binaries.pvt.build.mozilla.org/tooltool/"],
    "vcs_share_base": "/builds/hg-shared",
    "vcs_base_mirror_urls": ["http://hg-internal.dmz.scl3.mozilla.com"],
    "vcs_base_bundle_urls": ["http://ftp.mozilla.org/pub/mozilla.org/firefox/bundles"],
    "sendchange_masters": ["buildbot-master36.build.mozilla.org:9301"],
    "exes": {
        "tooltool.py": "/tools/tooltool.py",
        "buildbot": "/tools/buildbot-0.8.4-pre-moz2/bin/buildbot",
    },
    "env": {
        "CCACHE_DIR": "/builds/ccache",
        "CCACHE_COMPRESS": "1",
        "CCACHE_UMASK": "002",
        "SYMBOL_SERVER_HOST": "symbols1.dmz.phx1.mozilla.com",
        "SYMBOL_SERVER_USER": "b2gbld",
        "SYMBOL_SERVER_SSH_KEY": "/home/mock_mozilla/.ssh/b2gbld_dsa",
        "SYMBOL_SERVER_PATH": "/mnt/netapp/breakpad/symbols_b2g/",
        "POST_SYMBOL_UPLOAD_CMD": "/usr/local/bin/post-symbol-upload.py",
    },
    "purge_minsize": 10,
    "clobberer_url": "http://clobberer.pvt.build.mozilla.org/index.php",
    "is_automation": True,
}
