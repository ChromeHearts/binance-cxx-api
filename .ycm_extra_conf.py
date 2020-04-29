import os
import ycm_core

HOME = os.environ['HOME']


def FlagsForFile(filename, **kwargs):
    return {
        "flags": [
            "-Wall",
            "-Wextra",
            "-Wno-unused-variable",
            "-Wno-unused-parameter",
            "-I./include",
            "-I./ThirdParty/jsoncpp/include",
            "-I./ThirdParty/libwebsockets/include",
            "-I./ThirdParty/curl/include",
            "-I./ThirdParty/mbedtls/include",
            "-std=c++1z",
        ]
    }


def Settings(filename, **kwargs):
    return FlagsForFile(filename, **kwargs)
