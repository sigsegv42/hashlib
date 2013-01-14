{
  "targets": [
    {
      "target_name": "hashlib",
      "sources": [ 
        "hashlib.cc",
        "libhash/md4c.c", 
        "libhash/md5c.c",
        "libhash/sha0c.c"
      ],
      "defines": [
        "u_int32_t=uint32_t", 
        "u_int16_t=uint16_t"
      ],
      "include_dirs": [ "libhash" ],
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
