#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/spring-miuicamera',
]

blob_fixups: blob_fixups_user_type = {
    'system/priv-app/MiuiCamera/MiuiCamera.apk': blob_fixup()
        .apktool_patch('patches'),
}  # fmt: skip

# BEGIN SPRING JNI BUFFER OFFSET FIX
# Android 17 GraphicBuffer field offset, using the tested Spring binaries.
_spring_jni_key = 'system/lib64/libcamera_algoup_jni.xiaomi.so'
blob_fixups[_spring_jni_key] = (blob_fixups.get(_spring_jni_key, blob_fixup())
    .sig_replace('41 00 80 52 e3 03 1f 2a 08 ad 40 f9 00 01 3f d6 e8 03 40 f9', '41 00 80 52 e3 03 1f 2a 08 a9 40 f9 00 01 3f d6 e8 03 40 f9')
)
_spring_jni_key = 'system/lib64/libcamera_mianode_jni.xiaomi.so'
blob_fixups[_spring_jni_key] = (blob_fixups.get(_spring_jni_key, blob_fixup())
    .sig_replace('41 00 80 52 e3 03 1f 2a 08 ad 40 f9 00 01 3f d6 e8 03 40 f9', '41 00 80 52 e3 03 1f 2a 08 a9 40 f9 00 01 3f d6 e8 03 40 f9')
)
# END SPRING JNI BUFFER OFFSET FIX

module = ExtractUtilsModule(
    'spring-miuicamera',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
