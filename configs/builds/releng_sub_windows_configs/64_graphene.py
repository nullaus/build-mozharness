import os

config = {
    'default_actions': [
        'clobber',
        'clone-tools',
        'build',
        'update',  # may or may not happen based on query_is_nightly()
    ],
    'stage_platform': 'win64',
    'stage_product': 'graphene',
    'platform_supports_post_upload_to_latest': False,
    'enable_signing': False,
    'enable_talos_sendchange': False,
    'enable_count_ctors': False,
    'objdir': 'obj-graphene',
    'env': {
        'BINSCOPE': 'C:/Program Files (x86)/Microsoft/SDL BinScope/BinScope.exe',
        'HG_SHARE_BASE_DIR': 'C:/builds/hg-shared',
        'MOZBUILD_STATE_PATH': os.path.join(os.getcwd(), '.mozbuild'),
        'MOZ_AUTOMATION': '1',
        'MOZ_CRASHREPORTER_NO_REPORT': '1',
        'MOZ_OBJDIR': 'obj-firefox',
        'PATH': 'C:/mozilla-build/nsis-3.0a2;C:/mozilla-build/nsis-2.46u;C:/mozilla-build/python27;'
                'C:/mozilla-build/buildbotve/scripts;'
                '%s' % (os.environ.get('path')),
        'PROPERTIES_FILE': os.path.join(os.getcwd(), 'buildprops.json'),
        'TINDERBOX_OUTPUT': '1',
        'XPCOM_DEBUG_BREAK': 'stack-and-abort',
    },
    'src_mozconfig': 'b2g/graphene/config/mozconfigs/win64/nightly',
    #######################
}
