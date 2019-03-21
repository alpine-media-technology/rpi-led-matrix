{
  "targets": [
    {
      "target_name": "rpi-rgb-led-matrix-node",
      "sources": [
        "src/rpi-rgb-led-matrix.cc"
      ],
      'include_dirs': [
        "<!@(node -p \"require('node-addon-api').include\")",
        "./rpi-rgb-led-matrix/include"
      ],
      'dependencies': [
        "<!(node -p \"require('node-addon-api').gyp\")",
        "./binding.gyp:rpi-rgb-led-matrix"
      ],
      'cflags': [ '-Wall', '-Wextra', '-Wno-missing-field-initializers', '-Wno-unused-private-field', '-Wno-unused-variable' ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7',
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      },
    },
    {
			"target_name": "rpi-rgb-led-matrix",
			"type": "static_library",
			"sources": [
        "./rpi-rgb-led-matrix/lib/thread.cc",
        "./rpi-rgb-led-matrix/lib/pixel-mapper.cc",
        "./rpi-rgb-led-matrix/lib/options-initialize.cc",
        "./rpi-rgb-led-matrix/lib/multiplex-mappers.cc",
        "./rpi-rgb-led-matrix/lib/led-matrix-c.cc",
        "./rpi-rgb-led-matrix/lib/led-matrix.cc",
        "./rpi-rgb-led-matrix/lib/graphics.cc",
        "./rpi-rgb-led-matrix/lib/gpio.cc",
        "./rpi-rgb-led-matrix/lib/framebuffer.cc",
        "./rpi-rgb-led-matrix/lib/content-streamer.cc",
        "./rpi-rgb-led-matrix/lib/bdf-font.cc",
        "./rpi-rgb-led-matrix/lib/hardware-mapping.c"
			],
      "libraries": ["-lrt", "-lm", "-lpthread"],
      "include_dirs": [
        "./rpi-rgb-led-matrix/include"
      ],
      "direct_dependent_settings": {
        "include_dirs": [
          "./rpi-rgb-led-matrix/include"
        ]
      }
    }
  ]
}
