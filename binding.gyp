{
  "targets": [
    {
      "target_name": "libhash",
      "sources": [ 
        "libhash/md4c.c", 
        "libhash/md5c.c",
        "libhash/sha0c.c"
      ],
      "defines": [
        "u_int32_t=uint32_t", 
        "u_int16_t=uint16_t"
      ],
      "conditions": [
          ['OS=="win"', {
          }, { # OS != "win"
          "cflags": [ 
            "-O3"
          ]
        }]
      ]
    },
    {
      "target_name": "hashlib",
      "sources": [ "hashlib.cc" ],
      "dependencies": [ "libhash" ],
      "include_dirs": [ "libhash" ],
      "defines": [
        "u_int32_t=uint32_t", 
        "u_int16_t=uint16_t"
      ],
      "conditions": [
          ['OS=="win"', {
          }, { # OS != "win"
          "cflags": [ 
            "-O3"
          ]
        }]
      ]
    }
  ]
}
